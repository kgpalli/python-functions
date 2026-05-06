import wikipedia, warnings

warnings.filterwarnings('ignore', message='urllib3 v2 only supports OpenSSL')


def scrape(name="Microsoft",length=2):

    result = wikipedia.summary(name,sentences=length)
    return result


print(scrape("Facebook"))