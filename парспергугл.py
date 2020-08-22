import requests
import random
from config import bing_subscription_key

subscription_key = bing_subscription_key
search_url = "https://goto-bing.cognitiveservices.azure.com/bing/v7.0/images/search"

def getpics(search_term):
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "license": "public", "imageType": "photo"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    thumbnail_urls = [img["thumbnailUrl"]
                      for img in search_results["value"][:16]]
    if len(thumbnail_urls) > 0:
        return random.choice(thumbnail_urls)
    else:
        return None
