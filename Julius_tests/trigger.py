import time
import json
from datetime import datetime
import requests

#aws_api_url = "https://gffncchj4d.execute-api.us-east-1.amazonaws.com/test/trigger"
#aws_api_url = "https://ifl30z1ca5.execute-api.us-east-2.amazonaws.com/default/Stream_Video"
#aws_api_url = "https://1hltqctd35.execute-api.us-east-2.amazonaws.com/default/Predictor"
#With container
aws_api_url = "https://dttju25fc6.execute-api.us-east-2.amazonaws.com/default/julius"
# The callback for when a PUBLISH message is received from the server.
def trigger_lambda():

    # TRIGGER LAMBDA FUNCTION
    print("FUNCTION TRIGGERED!")
    req = requests.post(url=aws_api_url, data=json.dumps("")).json()
    print(req)
    #time.sleep(60)

trigger_lambda()