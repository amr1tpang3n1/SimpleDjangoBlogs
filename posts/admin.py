from django.contrib import admin
from posts.models import *


# Register your models here.
admin.site.site_header = "Ajay Blogs Admin Panel"
admin.site.register(Posts)

