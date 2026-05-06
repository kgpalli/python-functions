import my_lib.bot as bot
from click.testing import CliRunner
from wikibot import cli


def test_scrape(monkeypatch):
    monkeypatch.setattr(
        bot,
        "fetch_summary",
        lambda name, length: f"This is a mocked summary for {name}.",
    )
    result = bot.scrape("Microsoft", 2)
    assert "Microsoft" in result


def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Microsoft'])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output