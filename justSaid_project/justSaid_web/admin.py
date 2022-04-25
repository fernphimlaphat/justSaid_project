from django.contrib import admin
from .models import Post

admin.site.register(Post) # admin can access 'Post'
# Register your models here.
