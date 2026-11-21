#!/usr/bin/env python3

import shutil
import argparse
import enum
import os
import shlex
import subprocess
import pwd
from pathlib import Path
from pprint import pprint
from sys import path_importer_cache
from installers.neovim import install_neovim
from installers.flatpak import install_flatpaks


ROOT = Path(__file__).resolve().parent
STOW_DIR = ROOT / "stow"
PACKAGE_DIR = ROOT / "packages"
FONT_DIR = ROOT / "fonts"
SYSTEM_FONT_DIR = Path.home() / ".local/share/fonts"
HOME = Path.home()


def run(command: str, dry_run: bool = False) -> None:
    """
    Executes a system command.

    Args:
        command (list[str]): List of commands to be exectured.
        dry_run (bool): Determines if the set of commands is a "practice run",
        it wont delete or modify files if this is set to true.
    """
    split_command = shlex.split(command)

    print(
        f"{shlex.join(split_command)}", flush=True
    )  # Prints command to terminal and runs it.

    if dry_run:
        return

    if split_command[0] == "cd":
        os.chdir(split_command[1])
    else:
        subprocess.run(split_command, check=True)  # shows error if it occurs


def check_system() -> None:
    """
    Verifies the OS is Debian. Returns detected OS if not Debian.
    """

    OS_RELEASE = None

    for line in Path("/etc/os-release").read_text().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)

            if key == "ID":
                OS_RELEASE = value

    if OS_RELEASE != "debian":
        raise RuntimeError(
            f"This script is intended for Debian, instead found {OS_RELEASE}"
        )

    if os.geteuid() == 0:
        raise RuntimeError("Do not run this script as root.")


def install_oh_my_zsh(dry_run: bool = True) -> None:
    """
    Install Oh My Zsh without modifying .zshrc.
    """

    destination = Path.home() / ".oh-my-zsh"

    if destination.is_dir():
        print("Oh My Zsh is already installed.")
        return

    clone_git = (
        f"git clone --depth=1 https://github.com/ohmyzsh/ohmyzsh.git {str(destination)}"
    )

    run(clone_git, dry_run=dry_run)


def configure_zsh(dry_run: bool = True) -> None:
    """Set Zsh as the user's default login shell."""

    zsh = shutil.which("zsh")

    if zsh is None:
        if dry_run:
            print("Zsh is not installed yet; would configure it.")
            return
        raise RuntimeError("Zsh is not installed.")

    current_shell = pwd.getpwuid(os.getuid()).pw_shell

    if current_shell == zsh:
        print("Zsh is already the default login shell.")
        return

    run(f"chsh -s {zsh}", dry_run=dry_run)


def load_packages() -> list[str]:
    """
    Load package names from text files.
    """

    packages = []

    for file in PACKAGE_DIR.glob("*.txt"):
        for line in file.read_text().splitlines():
            line = line.split("#", 1)[0].strip()  # ignores comments

            if line:
                packages.extend(line.split())

    return list(dict.fromkeys(packages))


def load_modules() -> list[str]:
    """Find available Stow packages."""

    if not STOW_DIR.is_dir():
        return []

    return sorted(path.name for path in STOW_DIR.iterdir() if path.is_dir())


def install_packages(packages: list[str], dry_run: bool) -> None:
    """
    Install system packages through APT.
    """

    if not packages:
        return

    if dry_run:
        print("APT package installation skipped (dry run).")
        print("Would install", ", ".join(packages))
        return

    run("sudo apt-get update")
    run(f"sudo apt-get install {' '.join(packages)}")


def deploy_dotfiles(modules: list[str], dry_run: bool) -> None:
    """
    Deploy configuration files with GNU stow
    """

    if not modules:
        print("No Stow modules found.")
        return

    command = [
        "stow",
        "--verbose",
        "--no-folding",
        "--dir",
        str(STOW_DIR),
        "--target",
        str(HOME),
        *modules,
    ]

    command = f"stow --verbose --no-folding --dir {str(STOW_DIR)} --target {str(HOME)} {' '.join(modules)}"

    if not dry_run:
        run(command)


def install_fonts(dry_run: bool = False) -> None:
    """
    Install fonts from the dotfiles repository.
    """

    if not FONT_DIR.exists():
        print("No fonts directory found.")
        return

    fonts = [
        path
        for path in FONT_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in {".ttf", ".otf", ".ttc"}
    ]

    for font in fonts:
        destination = SYSTEM_FONT_DIR / font.relative_to(FONT_DIR)

        print(f"Installing: {font.name}")

        if dry_run:
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(font, destination)

    if fonts and not dry_run:
        subprocess.run(["fc-cache", "-f"], check=True)
        print("Font cache updated.")


def configure_bluetooth(dry_run: bool = True) -> None:
    command = "sudo systemctl enable --now bluetooth"
    run(command, dry_run=dry_run)


def detect_nvidia() -> bool:
    result = subprocess.run(
        ["lspci", "-n"],
        capture_output=True,
        text=True,
        check=True,
    )

    return any("10de:" in line.lower() for line in result.stdout.splitlines())


def configure_nvidia() -> None:
    if not detect_nvidia():
        print("No NVIDIA GPU detected.")
        return

    print("NVIDIA GPU detected.")
    print("Verify the appropriate maintained driver before installation.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bootstrap a Debian install")

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Install packages and deploy dotfiles.",
    )

    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying them.",
    )

    args = parser.parse_args()

    check_system()

    packages = load_packages()
    modules = load_modules()

    print(f"Found {len(packages)} packages.")
    print(f"Found {len(modules)} modules.")

    dry_run = not args.apply

    install_packages(packages, dry_run=dry_run)
    install_fonts(dry_run=dry_run)
    install_oh_my_zsh(dry_run)
    install_neovim(dry_run)
    install_flatpaks(dry_run)

    deploy_dotfiles(modules, dry_run=dry_run)
    configure_bluetooth(dry_run)

    if dry_run:
        print("Dry run complete. No changes made.")
    else:
        print("Bootstrap complete")
