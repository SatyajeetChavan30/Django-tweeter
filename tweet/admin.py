from django.contrib import admin
from .models import tweet
from .models import contact_me
# Register your models here.

admin.site.register(tweet)
admin.site.register(contact_me)
