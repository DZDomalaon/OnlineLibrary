from django.contrib import admin
from .models import Books, BookComments, BookCheckout
# Register your models here.

admin.site.register(Books)
admin.site.register(BookComments)
admin.site.register(BookCheckout)