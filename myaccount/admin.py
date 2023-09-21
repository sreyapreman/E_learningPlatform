from django.contrib import admin
from app.models import Course,Demo_video
from myaccount.models import Users

admin.site.register(Course)
admin.site.register(Demo_video)
admin.site.register(Users)
