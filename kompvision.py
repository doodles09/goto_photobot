import requests
from config import vision_subscription_key

def vision(file):
    endpoint = "https://goto-vision.cognitiveservices.azure.com/"
    subscription_key = vision_subscription_key
    analyze_url = endpoint + "vision/v3.0/analyze"

    # Set image_path to the local path of an image that you want to analyze.
    # Sample images are here, if needed:
    # https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images
    image_path = file

    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json()
    # print(analysis)
    return analysis["description"]["captions"][0]["text"].capitalize()
    # print(image_caption)
