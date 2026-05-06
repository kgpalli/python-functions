"""Simple Wikipedia scraping helper."""

import wikipedia

def scrape(name="Microsoft", length=2):
    """Return a short Wikipedia summary for the given page name."""
    result = wikipedia.summary(name, sentences=length)
    return result


print(scrape("Facebook"))
