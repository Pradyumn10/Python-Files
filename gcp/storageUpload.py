'''
* @FileName : storageUpload.py
* @author : Pradyumn Joshi
* @brief : Uploading the file to google storage
* @version : 0.1.0
*
* @copyright (c) 2021
'''
import io
from io import BytesIO
import pandas as pd
from google.cloud import storage

storage_client = storage.Client.from_service_account_json("json key")

# create a Bucket list

bucket = storage_client.get_bucket("bucket1_joshi")

image = "photo-of-neon-signage-1820770.jpg"
filename = "%s%s" % ('',image)
blob = bucket.blob(filename)

with open(image, 'rb') as f:
    blob.upload_from_file(f)

print("upload complete")

