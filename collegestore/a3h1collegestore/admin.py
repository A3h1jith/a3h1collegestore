from django.contrib import admin
from django.contrib.auth.models import User

from a3h1collegestore.models import Department, Course, Message

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Message)