from pathlib import Path
import pathlib
import shlex
import subprocess


def run(command: list[str], dry_run: bool = False) -> None:
    """
    Exectuse a system command.

    Args:
        command (list[str]): List of commands to be exectured.
        dry_run (bool): Determines if the set of commands is a "practice run",
        it wont delete or modify files if this is set to true.
    """

    print(
        f"{shlex.join(command)}", flush=True
    )  # Prints command to terminal and runs it.

    if not dry_run:
        subprocess.run(command, check=True)  # shows error if it occurs


def install_neovim(dry_run: bool = True) -> None:
    """
    Install Neovim 0.12.6
    """

    git_repo = "https://github.com/neovim/neovim"

    clone_repo = [
        "git",
        "clone",
        git_repo,
    ]

    change_directory = [
        "cd",
        "neovim",
    ]

    make = [
        "make",
        "CMAKE_BUILD_TYPE=RelWithDebInfo",
    ]

    install = [
        "sudo",
        "make",
        "install",
    ]

    run(clone_repo, dry_run=dry_run)
    run(change_directory, dry_run=dry_run)
    run(make, dry_run=dry_run)
    run(install, dry_run=dry_run)
