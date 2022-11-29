from django.db import models

class Post(models.Model):
    class Meta(object):
        db_table = 'main'

    name = models.CharField (
        'Name',blank = False, null =False , max_length = 15, default='Anonymous'
    )
    address = models.TextField (
        'Address',blank = True, null =True , max_length = 40
    )