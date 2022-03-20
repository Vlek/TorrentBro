"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main(prog_name: str) -> None:
    """Torrentbro."""


if __name__ == "__main__":
    main(prog_name="TorrentBro")  # pragma: no cover
