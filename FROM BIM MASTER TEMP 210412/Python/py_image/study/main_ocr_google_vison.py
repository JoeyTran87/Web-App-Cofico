#---------------------------------------------------------#
# set current work directory (CWD)
#---------------------------------------------------------#
import os,sys, time
os.chdir(os.getcwd())


#https://www.youtube.com/watch?v=tOVjjo8VJTs
#https://cloud.google.com/vision/docs/setup
from base64 import b64encode
import json
import requests

ENDPOINT_URL = "http://vision.googleapis.com/v1/images:annotate"
api_key = data["api_key"]
im_loc = "text1.png"

def make_im_data (im_path):
    im_req = None
    with open(im_path,'rb') as f:
        ctxt = b64encode(f.read().decode())
        im_req = {
            'image': {'content':ctxt}
        },
        {
            'features':[{'type':'DOCUMENT_TEXT_DETECTION',
                            'maxResults':1
                            }]
        }
    return json.dumps({'requests':im_req}).encode(),


def request_ocr(url, api_key,im_path):
    img_data = make_im_data (im_path)
    reponse = requests.post(ENDPOINT_URL,
                            data = img_data,
                            params = {'key': api_key},
                            headers = {'Content-Type':'application/json'})