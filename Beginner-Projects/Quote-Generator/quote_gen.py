import requests

# Fetch a random quote from ZenQuotes API
response = requests.get("https://zenquotes.io/api/random")

# Parse the JSON response
if response.status_code == 200:
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    print("Quote of the Day")
    print(f"\"{quote}\" – {author}")
else:
    print("Oops! Couldn't fetch a quote right now.")