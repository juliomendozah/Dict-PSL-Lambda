import io
from boto3.session import Session
import time
import numpy as np
import cv2

filepath="ira_alegria.mp4"
filepath_local="test2.mp4"

session= Session(
    region_name=#,
    aws_access_key_id=#,
    aws_secret_access_key=#
)
s3 = session.resource("s3")

BUCKET="jolepe"
PATH="ira_alegria.mp4"

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
    decoded = cv2.imdecode(np.frombuffer(stream.getvalue(), np.uint8), -1)

    print('OpenCV:\n', type(decoded))
    #print(np_stream.shape)
    bytes_stream2mp4(stream, filepath_local)

    print("--Bytes Stream to MP4 conversion finished--")


start_time = time.time()
main()
print("--- Program's Execution Time: %s seconds ---" % (time.time() - start_time))
