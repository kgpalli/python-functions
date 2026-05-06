from wikibot import scrape

def test_scrape():
    assert "facebook" in scrape("Facebook")