from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia for a given name."""
    print(f"Searching Wikipedia for '{name}'...")

    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize a Wikipedia page."""
    print(f"Summarizing Wikipedia page for '{name}'...")

    summary = wikipedia.summary(name)
    return summary

def get_text_blob(text):
    """Convert text to a TextBlob object."""
    print("Converting text to TextBlob...")
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name and return  back phrases."""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    return blob.noun_phrases

golden_state_warriors_text = wikipedia.summary("Golden State Warriors")