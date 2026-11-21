from pathlib import Path
import pathlib
import os
import shlex
import subprocess


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


def install_neovim(dry_run: bool = True) -> None:
    """
    Install Neovim 0.12.6
    """
    command_list = []

    git_repo = "https://github.com/neovim/neovim"

    clone_repo = command_list.append(f"git clone {git_repo} /usr/local/src/")
    change_directory = command_list.append("cd /usr/src/neovim")
    make = command_list.append("make CMAKE_BUILD_TYPE=RelWithDebInfo")
    install = command_list.append("sudo make install")

    for command in command_list:
        run(command, dry_run)


def setup_neovim(dry_run: bool = True) -> None:
    """
    Install neovim specific things (tree-sitter, pynvim, etc.)
    """

    """
    need to install the correct up-to-date rust install
    `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
    then run `cargo install tree-sitter-cli`
    """


def setup_python_env(dry_run: bool = True) -> None:
    """
    Creates python venv for whole system that is selected upon boot
    """

    command_list = []

    libraries = [
        "numpy",
        "scipy",
        "matplotlib",
        "pandas",
    ]

    create_directory = command_list.append("mkdir -p ~/.venvs")
    create_venv = command_list.append("python3 -m venv ~/.venvs/global")
    source_venv = command_list.append("source ~/.venvs/global/bin/activate")
    install_pip = command_list.append("python -m pip install --upgrade pip")
    install_libraries = command_list.append(f"pip install {' '.join(libraries)}")

    for command in command_list:
        run(command, dry_run)


if __name__ == "__main__":
    setup_python_env()
