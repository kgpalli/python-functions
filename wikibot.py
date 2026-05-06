"""Simple Wikipedia scraping helper."""

from my_lib.bot import scrape
import click

@click.command()
@click.option("--name", default="Microsoft", help="The Wikipedia page to scrape.")


def cli(name):
    """Scrape a Wikipedia summary."""
    result = scrape(name)
    click.echo(click.style(result, fg="blue", bg="white", bold=True))


if __name__ == "__main__":
    cli()
