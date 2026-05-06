"""Simple Wikipedia scraping helper."""

import wikipedia


def fetch_summary(name: str = "Microsoft", length: int = 2) -> str:
    """Return a short Wikipedia summary from the wikipedia package."""
    return wikipedia.summary(name, sentences=length)


def scrape(name: str = "Microsoft", length: int = 2) -> str:
    """Return a short Wikipedia summary for the given page name."""
    return fetch_summary(name, length)


if __name__ == "__main__":
    print(scrape("Facebook"))
