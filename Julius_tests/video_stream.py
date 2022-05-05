import time
import json
from datetime import datetime
import requests

#aws_api_url = "https://gffncchj4d.execute-api.us-east-1.amazonaws.com/test/trigger"
#aws_api_url = "https://ifl30z1ca5.execute-api.us-east-2.amazonaws.com/default/Stream_Video"
#aws_api_url = "https://1hltqctd35.execute-api.us-east-2.amazonaws.com/default/Predictor"
aws_api_url = "https://6faug0ia73.execute-api.us-east-2.amazonaws.com/test/"
bucket="jolepe"
file_path = "Videos/temp.mp4"
file=file_path.split("/")[1]
# The callback for when a PUBLISH message is received from the server.
def upload_video():

    print("VIDEO UPLOADED!")
    headers = {'Content-type': 'video/mp4'}
    payload = open(file_path, 'rb')
    req = requests.request("PUT", aws_api_url+bucket+"/"+file, headers=headers, data=payload)
    print(req)

upload_video()