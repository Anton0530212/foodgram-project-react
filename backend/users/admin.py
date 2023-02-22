from django.contrib import admin
from .models import User, Subscription
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Subscription)
