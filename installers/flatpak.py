from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent


def install_flatpaks(dry_run: bool = True) -> None:
    """
    Install Flatpak applications listed in a manifest.
    """

    manifest = ROOT / "packages" / "flatpak.txt"

    if not manifest.exists():
        return

    apps = [line.split("#", 1)[0].strip() for line in manifest.read_text().splitlines()]

    apps = [app for app in apps if app]

    if dry_run:
        print(f"Would install Flatpaks: {apps}")
        return

    subprocess.run(
        [
            "flatpak",
            "remote-add",
            "--user",
            "--if-not-exists",
            "flathub",
            "https://dl.flathub.org/repo/flathub.flatpakrepo",
        ],
        check=True,
    )

    for app in apps:
        subprocess.run(
            [
                "flatpak",
                "install",
                "--user",
                "--assumeyes",
                "flathub",
                app,
            ],
            check=True,
        )
