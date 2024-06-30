from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    status = models.IntegerField(null=True)
    
    def __str__(self):
        return "{}".format(self.username)

    empAuth_objects = models.Manager()

# class Meta:
#     db_table = 'tbl_authentication'