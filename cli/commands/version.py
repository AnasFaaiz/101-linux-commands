import typer
from __version__ import __version__

app = typer.Typer(help="version command")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Show the current version of 101-linux CLI"""
    if ctx.invoked_subcommand is None:
        typer.echo(f"101-linux v{__version__}")

@app.command()
def show():
    """Show the current version of 101-linux CLI"""
    typer.echo(f"101-linux v{__version__}")
