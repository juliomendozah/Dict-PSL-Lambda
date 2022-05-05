import io
from boto3.session import Session
import time
import numpy as np
#import cv2
import json

filepath="ira_alegria.mp4"
filepath_local="test2.mp4"

session= Session(
    region_name='us-east-2',
    aws_access_key_id='AKIAT3I4RTHMRMKWPIPS',
    aws_secret_access_key='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'
)
s3 = session.resource("s3")

BUCKET="jolepe"
PATH="temp.mp4"

def lambda_handler(event, context):
    # TODO implement

    start_time = time.time()
    main()
    return {
        'statusCode': 200,
        'body': json.dumps("--- Program's Execution Time: %s seconds ---" % (time.time() - start_time))
    }

def generate_bytes_stream(filepath):
    with open(filepath, 'rb') as fh:
        stream = io.BytesIO(fh.read())
    return stream

def bytes_stream2mp4(stream,filepath_local):
    with open(filepath_local, 'wb') as local_file:
        local_file.write(stream.getbuffer())

def get_s3_stream(s3,BUCKET,PATH):

    stream = io.BytesIO()
    s3_object = s3.Object(BUCKET, PATH)
    print(s3_object)
    s3_object.download_fileobj(stream)
    stream.seek(0)

    return stream

def main():

    stream=get_s3_stream(s3,BUCKET,PATH)
    #print(stream.getvalue())
    #Bytes to numpy
    print(type(stream.getvalue()))
    #np_stream = np.load(stream.getvalue(), allow_pickle=True,encoding = 'bytes')
    #decoded = cv2.imdecode(np.frombuffer(stream.getvalue(), np.uint8), -1)

    #print('OpenCV:\n', type(decoded))
    #print(np_stream.shape)
    bytes_stream2mp4(stream, filepath_local)

    print("--Bytes Stream to MP4 conversion finished--")


