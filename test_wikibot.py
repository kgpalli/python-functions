import wikibot


def test_scrape(monkeypatch):
    monkeypatch.setattr(
        wikibot,
        "fetch_summary",
        lambda name, length: "Facebook is a social network.",
    )

    result = wikibot.scrape("Facebook")
    assert "facebook" in result.lower()