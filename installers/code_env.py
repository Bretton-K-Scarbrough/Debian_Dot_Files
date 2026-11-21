from pathlib import Path
import pathlib
import os
import shlex
import subprocess

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


def install_neovim(dry_run: bool = True) -> None:
    """
    Install Neovim 0.12.6
    """
    command_list = []

    git_repo = "https://github.com/neovim/neovim"
    src_directory = HOME / "usr/local/src/neovim"

    clone_repo = command_list.append(f"git clone {git_repo} {src_directory}")
    change_directory = command_list.append(f"cd {src_directory}")
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

    command_list = []

    install_rust = command_list.append(
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
    )
    install_tree_sitter = command_list.append("cargo install tree-sitter-cli")

    for command in command_list:
        run(command, dry_run)


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

    venvs_directory = HOME / "/.venvs"
    global_venv_directory = venvs_directory / "global"
    activate_directory = global_venv_directory / "/bin/activate"

    create_directory = command_list.append(f"mkdir -p {venvs_directory}")
    create_venv = command_list.append(f"python3 -m venv {global_venv_directory}")
    source_venv = command_list.append(f"source {activate_directory}")
    install_pip = command_list.append("python -m pip install --upgrade pip")
    install_libraries = command_list.append(f"pip install {' '.join(libraries)}")

    for command in command_list:
        run(command, dry_run)


def setup_code_env(dry_run: bool = True) -> None:
    setup_python_env(dry_run)
    install_neovim(dry_run)
    setup_neovim(dry_run)


if __name__ == "__main__":
    setup_python_env()
