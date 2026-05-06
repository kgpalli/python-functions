"""Simple Wikipedia scraping helper."""

import click
from my_lib.bot import scrape

@click.command()
@click.option("--name", default="Microsoft", help="The Wikipedia page to scrape.")
@click.option("--length", default=2, help="Number of sentences to return.")
def cli(name: str, length: int):  # pylint: disable=E1120
    """Scrape a Wikipedia summary."""
    result = scrape(name, length)
    click.echo(click.style(result, fg="blue", bg="white", bold=True))


if __name__ == "__main__":
    cli()
