import urllib.request,json

def get_quotes():
    response = urllib.request.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        return quote