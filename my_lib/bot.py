import wikipedia

def fetch_summary(name: str = "Microsoft", sentences: int = 2) -> str:
    """Return a short Wikipedia summary from the wikipedia package."""
    try:
        return wikipedia.summary(name, sentences=sentences)
    except Exception as e:
        return f"Error fetching summary for '{name}': {str(e)}"


def scrape(name: str = "Microsoft", length: int = 2) -> str:
    """Return a short Wikipedia summary for the given page name."""
    return fetch_summary(name, sentences=length)