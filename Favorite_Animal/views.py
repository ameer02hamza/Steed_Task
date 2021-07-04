from django.shortcuts import render
import os
import pyrebase
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

config = {
    "apiKey": "AIzaSyDEar-FYtHHHvvSdHe8_qHO1SqfzNN8UPY",
    "authDomain": "animals-55847.firebaseapp.com",
    "projectId": "animals-55847",
    "databaseURL": "https://animals-55847-default-rtdb.firebaseio.com/",
    "storageBucket": "animals-55847.appspot.com",
    "messagingSenderId": "909409559603",
    "appId": "1:909409559603:web:0a2ac735b7e36841fdef46",
    "measurementId": "G-GY1P9DDGDX"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


class UserSignUp(ViewSet):
    """
    users will Register themself by using the firebase authentication
    """

    def signup(self, *args, **kwargs):
        email = self.request.data['email']
        password = self.request.data['password']
        try:
            print("34", password, email)
            user = authe.create_user_with_email_and_password(email, password)
            print("36")
            user_id = user['localId']
            print(user_id)
        except:
            return Response({"Failed": "Unsuccessful"})

        return Response({"Successfully Registered": self.request.data})


class UserSignIn(ViewSet):
    """
    user will signin by using the firebase authentication
    """

    def signin(self, *args, **kwargs):
        email = self.request.data['email']
        password = self.request.data['password']
        try:
            user = authe.sign_in_with_email_and_password(email, password)
            user_id = user['localId']
            print(user_id)
        except:
            return Response({"Failed": "Invalid Credentials"})
        return Response({"Success": "You are successfully logged In"})


class AddAnimal(ViewSet):
    """
     user can add and remove their favorite animals from list
    """

    def post(self, *args, **kwargs):
        print(self.request.data)
        try:
            database.child("Data").push({
                "Id": self.request.data['id'],
                "Name": self.request.data['Name'],
                "Age": self.request.data['age'],
                "price": self.request.data['price']

            })
        except:
            return Response({"Failed": "Unable to save record"})

        data = {
            "Success": self.request.data,
        }
        return Response(data)

    def delete(self, *args, **kwargs):
        try:
            database.child("Data").child(self.request.data['Hash']).remove()
            data = {
                "Success": "record deleted",
                "Data": self.request.data
            }
        except:
            return Response({"Failed": "Failed to delete record"})

        return Response(data)
