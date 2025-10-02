"""Main CLI entry point for 101-linux-commands."""

import typer

from commands import hello, version

# Create the root CLI app
app = typer.Typer(help="101 Linux Commands CLI 🚀")

# Register subcommands
app.add_typer(hello.app, name="hello")
app.add_typer(version.app, name="version")


if __name__ == "__main__":
    app()
