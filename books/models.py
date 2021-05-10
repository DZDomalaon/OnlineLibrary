from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import CustomUser

# Create your models here.
class Books(models.Model):

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    location = models.CharField(max_length=250, blank=True, null=True)
    book_image = models.ImageField(blank=True, null=True, upload_to='books/', default='books/default.png')
    is_digital = models.BooleanField(default=False)    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, default='available')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)           

    def __str__(self):
        return self.title


class BookComments(models.Model):
    
    comment = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book_comment = models.ForeignKey(Books, on_delete=models.CASCADE)    

    def __str__(self):
        return self.comment


class BookCheckout(models.Model):

    checkedout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True, auto_now=False) 
    is_returned = models.BooleanField(default=False)
    borrower = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    book_checkout = models.ForeignKey(Books, on_delete=models.CASCADE)          

    def __str__(self):
        return str(self.checkedout_date)
