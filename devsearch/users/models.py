from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key = True, 
                        default = uuid.uuid4, 
                        unique = True, 
                        editable = False)
    user = models.OneToOneField(User, 
                                on_delete = models.CASCADE, 
                                null = True, 
                                blank = True)
    username = models.CharField(max_length =200,
                                null = True, 
                                blank = True)
    name = models.CharField(max_length =200,
                            null = True, 
                            blank = True)
    email = models.EmailField(max_length =200,
                              null = True, 
                              blank = True)
    short_intro = models.CharField(max_length =200,
                                   null = True, 
                                   blank = True)
    bio = models.TextField(max_length =200,
                           null = True, 
                           blank = True)
    profile_image = models.ImageField(null = True, 
                                      blank = True,
                                      upload_to = "profiles/",
                                      default = "profiles/user-default.png")
    social_github = models.CharField(max_length =200,
                                     null = True, 
                                     blank = True)
    social_twitter = models.CharField(max_length =200,
                                      null = True, 
                                      blank = True)
    social_linkedin = models.CharField(max_length =200,
                                       null = True, 
                                       blank = True)
    social_youtube = models.CharField(max_length =200,
                                      null = True, 
                                      blank = True)
    social_website = models.CharField(max_length =200,
                                      null = True, 
                                      blank = True)
    created = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        """_summary_
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        """
        return str(self.user.username)