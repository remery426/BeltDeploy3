from __future__ import unicode_literals

from django.db import models

from ..login_app.models import User
from datetime import date
import datetime

class tripManager(models.Manager):
    def add(self,postData,user_id):
        response = {}
        errors = []
        if len(postData['destination'])<1 or len(postData['description'])<1 or len(postData['date_from'])<1 or len(postData['date_until'])<1:
            errors.append('All fields are mandatory!')
        try:
            datetime.datetime.strptime(postData['date_from'], '%Y-%m-%d')
            if postData['date_from']<str(datetime.date.today()):
                errors.append("Trip start date has past!")
        except ValueError:
            errors.append("Please enter date format YYYY-MM-DD")
        try:
            datetime.datetime.strptime(postData['date_until'], '%Y-%m-%d')
            if postData['date_until']<postData['date_from']:
                errors.append("Trip cannot end before it begins!")
        except ValueError:
            errors.append("Please enter date in format YYYY-MM-DD")
        if errors:
            response['error']=errors
            response['status']= False
            return response
        trip =self.create(destination=postData['destination'], description=postData['description'], datefrom = postData['date_from'], dateuntil=postData['date_until'], user = user_id  )
        trip.userlist.add(user_id)
        response['status']=True
        return response
class Trip(models.Model):
    destination = models.TextField(max_length =100)
    description = models.TextField(max_length=300)
    datefrom = models.DateField(null=True)
    dateuntil = models.DateField(null=True)
    user = models.ForeignKey(User)
    userlist = models.ManyToManyField(User, related_name = "userlist")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = tripManager()
