from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile



# @receiver(post_save, sender = Profile)
def create_profile(sender, instance, created, **kwargs):
    """If the account is a new user, create the user in the main 
    Django users database and create a profile for that user"""
    
    if created:
        user = instance
        profile = Profile.objects.create(user = user, 
                                         username = user.username, 
                                         email = user.email, 
                                         name = user.first_name)


post_save.connect(create_profile, sender = User)


# @receiver(post_delete)
def delete_profile(sender, instance, **kwargs):
    """If the user profile is deleted, this function will also delete 
    the user account that is stored in the main Django users database."""
    
    user = instance.user
    user.delete()


post_delete.connect(delete_profile, sender = Profile)


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        

post_save.connect(update_user, sender=Profile)