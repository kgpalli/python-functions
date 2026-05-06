from my_lib.bot import scrape
from click.testing import CliRunner
from wikibot import cli


def test_scrape(monkeypatch):
    monkeypatch.setattr(
        bot,
        "fetch_summary",
        lambda name: f"This is a mocked summary for {name}.",
    )
    assert "Microsoft" in scrape("Microsoft")
    
def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name','Microsoft'])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output