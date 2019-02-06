import json
import requests
import os

def handler(event, context):

    res = requests.get('http://www.google.com')
    res = {
        "message": "Wonderful! This is a cat fact 1!",
        "google msg":res.text[:20], 
        "event": event
    }
    print('myvar:', os.environ['MYVAR'])
    print(res)
    return res
