"""
  @file upload_data.py
  @author Pradyumn Joshi
  @brief It uploads data from device to Google Cloud Platform
  @version 0.1.0
  @date 2020-07-21

  @copyright Copyright (c) 2020

 """
from google.cloud import pubsub_v1
import json
import time
import datetime
import pyrebase
import os
from threading import Thread
import io
from gcloud import storage


class threading_cloud:
    """
    Threading for cloud class
    """

    def __init__(self):
        """
        Construcor for threading class
        Created a object for cloud class
        """
        self.cloud_obj = cloud()

    def run_data(self,pos,neg,accu):
        """
        Thread to upload data

        Args:
            pos (int): Wearing a Mask sends 1 if not then 0
            neg (int): Not Wearing Mask sends 0 if yes then 1
            accu (float): Detection accuracy percentage 
        """
        thread1 = Thread(
                target=self.cloud_obj.upload, 
                args=(pos, neg, accu))
        thread1.start()
    
    def run_image_firebase(self,without_mask,without_mask_str):
        """
        Thread to upload image on firebase

        Args:
            without_mask (int): Image name on device
            without_mask_str (str): Image name on cloud
        """
        thread2 = Thread(
                target=self.cloud_obj.upload_image_firebase, 
                args=(without_mask, without_mask_str))
        thread2.start()

    def run_image_storage(self, without_mask, without_mask_str):
        """
        Thread to upload image on gcp storage

        Args:
            without_mask (int): Image name on device
            without_mask_str (str): Image name on cloud
        """
        thread3 = Thread(
                target=self.cloud_obj.upload_image_storage,
                args=(str(without_mask), str(without_mask_str)))
        thread3.start()
    


class cloud:
    """
    Class which uploads data and images on Google Cloud Platform
    """
    def __init__(self):
        """
        Constructor for class cloud. 
        """
        
        self.deviceAddress = "Robro Systems, Dewas Naka, Indore"      #address of device deployment
        self.project_id = "robro-trial2"                    #Google Project ID
        self.topic_name = "topics"                          #pub-sub topic name
        self.futures = dict()
        self.data = dict()
        
        # storage configuration
        self.storage_client = storage.Client.from_service_account_json("/home/robro/Kiara/kiara_general/kiara/robro-trial2-a58a028c1c86.json", project='robro-trial2')                                                      #json file, project name
        self.bucket = self.storage_client.get_bucket("bucket1_robro")        #bucket name
        
        # firebase configuration
        self.config = {
        "apiKey" : "AIzaSyCHQV8JxqXT0QewKAlB0Fkyh0qaXiGeZmg",
        "authDomain" : "robro-trial2.firebaseapp.com",
        "databaseURL": "https://robro-trial2.firebaseio.com",
        "projectId": "robro-trial2",
        "storageBucket": "robro-trial2.appspot.com",
        "messagingSenderId": "443528895102",
        "appId": "1:443528895102:web:f80bc2375af7de58c5962f",
        "measurementId" : "G-SKHX2L18VZ"
    }
        # initializing firebase
        self.firebase = pyrebase.initialize_app(self.config)
        self.storage = self.firebase.storage()
    
    def get_callback(self,dictOfFutures, data):
        """
        Publish errors are handled with this function

        Args:
            dictOfFutures (dict): Dictionary of futures
            data (dict): Dictionary of data uploaded
        """
        def callback(dictOfFutures):
            try:
                # print(f.result())
                self.futures.pop(data)
            except:
                print("\n\t\tException!!\n")
                # print("Please handle {} for {}."
                #        .format(f.exception(), data))
     
        return callback
    

    
    def upload(self, pos,neg,accuracy):
        """
        Uploading data on cloud

        Args:
            pos (int): Wearing a Mask sends 1 if not then 0
            neg (int): Not Wearing Mask sends 0 if yes then 1
            accu (float): Prediction accuracy percentage
        """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/robro/Kiara/kiara_general/kiara/robro-trial2-a58a028c1c86.json"   #exporting json file
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project_id, self.topic_name)
        dateValue = float(time.time())                   #dates
        timeValue = time.strftime("%H:%M:%S",time.localtime())       #time
            # location
          
        self.data = {"count_pos":pos, 
                "count_neg":neg, 
                "accuracy":accuracy, 
                "dates":dateValue, 
                "time":timeValue, 
                "locations":self.deviceAddress
                }

        # print(self.data)
        
        # When you publish a message, the client returns a future. "Data Uploaded"
        self.future = publisher.publish(
            topic_path, data=(json.dumps(self.data)).encode("utf-8")) # data must be a bytestring.

        # Publish failures shall be handled in the callback function.
        self.future.add_done_callback(self.get_callback(self.future, self.data))
        """ 
        # Wait for all the publish futures to resolve before exiting.
        while futures:
            time.sleep(0.2)
     
        print("Published message with error handler.")
        """
    
    
    def upload_image_firebase(self, without_mask, without_mask_str):
        """
        Uploading images to firebase storage

        Args:
            without_mask (int): Image name on device
            without_mask_str (str): Image name on cloud 
        """
        path = "/home/robro/Kiara/kiara_general/kiara/collect_data/without_mask/"                           #path to images
        self.storage.child("images/{}".format(without_mask_str)).put("{}.jpg".format(path+without_mask))    #{location:firebase ; local_location/image_name}



    
    def upload_image_storage(self, without_mask, without_mask_str):
        """
        Uploading images to google storage bucket

        Args:
            without_mask (int): Image name on device
            without_mask_str (str): Image name on cloud
        """
        path = "/home/robro/Kiara/kiara_general/kiara/collect_data/without_mask/{}.jpg".format(without_mask)  #path to images
        # image = path+without_mask
        filename = "%s%s" % ('',path)
        blob = self.bucket.blob("six/{}.jpg".format(without_mask_str))                                        #path of gcp storage
        blob.content_type = "image/jpeg"                                                                      #meta-data content type for images

        with open(path, 'rb') as f:
            blob.upload_from_file(f)
        print("Image Uploaded : ", without_mask_str)

