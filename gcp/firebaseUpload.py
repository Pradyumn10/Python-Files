'''
* @FileName : firebaseUpload
* @author : Prayumn Joshi
* @brief : It uploads file to google firebase
* @version : 0.1.0
*
* @copyright (c) 2021
'''
#pyrebase library of firebase = python+firebase

import pyrebase

config = {
        "apiKey" : "AIzaSyDKV3uwzCoOpo7JnlS4OjfKQKFS0q650SM",
        "authDomain" : "robro-demo1.firebaseapp.com",
        "databaseURL" : "https://robro-demo1.firebaseio.com",
        "projectId" : "robro-demo1",
        "storageBucket" : "robro-demo1.appspot.com",
        "messagingSenderId" : "139258920201"
        }
#initializing firebase {pyrebase}
firebase = pyrebase.initialize_app(config)

#initializing storage varible
storage = firebase.storage()
#uploading the image to firebase database
storage.child("images/3.jpg").put("image3.jpg")

#printing the url of images
#print(storage.child("images/0.jpg").get_url(None))


