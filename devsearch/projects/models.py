from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    """ Create a simple table to add some example data into.
    """
    id = models.UUIDField(primary_key = True, 
                          default = uuid.uuid4, 
                          unique = True, 
                          editable = False)
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True, 
                                   blank = True)
    demo_link = models.CharField(max_length = 2000, 
                                 null = True, 
                                 blank = True)
    source_link = models.CharField(max_length = 2000, 
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