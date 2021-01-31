from django.db import models



class Users(models.Model):
    user_id = models.TextField(max_length=20, blank=True)
    user_name=models.TextField(max_length=20,blank=True)
    birthday=models.DateField(auto_now=False, auto_now_add=False)
    join_time = models.DateField(auto_now=False, auto_now_add=True)
    status = models.DateField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.user_id
