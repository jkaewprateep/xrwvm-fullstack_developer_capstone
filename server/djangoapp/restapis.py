# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    # 'backend_url', default="http://localhost:8000")
    'backend_url', default="https://jkaewprateep-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai")    

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    # default="http://localhost:5050/"
    default="https://sentianalyzer.1habef5v6cec.us-south.codeengine.appdomain.cloud"
    )

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    if len(params) < 6 :
        request_url = backend_url+str(endpoint).strip();
    else :
        request_url = backend_url+str(endpoint).strip()+"?"+params

    # print("***", request_url)
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        # print("***", response)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"/analyze/"+text

    print("***", request_url)

    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")