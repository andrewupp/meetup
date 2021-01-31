from django.db import models



class MapUser(models.Model):
    user_id = models.TextField(max_length=20, blank=True)
    user_name=models.TextField(max_length=20,blank=True)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    long= models.DecimalField(max_digits=10, decimal_places=7)
    last_updated = models.DateTimeField(auto_now_add=True)
    description = models.CharField( max_length=100, null=True)

    def __str__(self):
        return self.user_id
