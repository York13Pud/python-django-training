from django.db import models
from users.models import Profile

# Create your models here.
class Project(models.Model):
    """ Define a simple model to add some example data into."""
    
    id = models.UUIDField(primary_key = True, 
                          default = uuid.uuid4, 
                          unique = True, 
                          editable = False)
    owner = models.ForeignKey(Profile, 
                              null = True, 
                              blank = True, 
                              on_delete = models.SET_NULL)
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True, 
                                   blank = True)
    featured_image = models.ImageField(null = True,
                                       blank = True,
                                       default = "default.jpg")
    demo_link = models.CharField(max_length = 2000, 
                                 null = True, 
                                 blank = True)
    source_link = models.CharField(max_length = 2000, 
                                   null = True, 
                                   blank = True)
    tag = models.ManyToManyField("Tag",
                                 blank = True)
    vote_totals = models.IntegerField(default = 0, 
                                      null = True, 
                                      blank = True)
    vote_ratio = models.IntegerField(default = 0, 
                                     null = True, 
                                     blank = True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """_summary_
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        """
        return self.title


class Review(models.Model):
    """Define a model for a table that will contain data about project reviews."""
    
    VOTE_TYPE = (
        ("Up", "Up Vote"),
        ("Down", "Down Vote"),
    )
    id = models.UUIDField(primary_key = True, 
                        default = uuid.uuid4, 
                        unique = True, 
                        editable = False)
    # owner = 
    project = models.ForeignKey(Project,  
                                on_delete = models.CASCADE)
    body = models.TextField(null=True, 
                            blank = True)
    value = models.CharField(max_length = 200,
                             choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """_summary_
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        """
        return self.value


class Tag(models.Model):
    """Define a model for a table that will contain all the names of tags that can be used."""
    id = models.UUIDField(primary_key = True, 
                          default = uuid.uuid4, 
                          unique = True, 
                          editable = False)
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """_summary_
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        Returns:
            This returns a string representation of the title in the admin panel for a row, rather than the object description.
        """
        return self.name