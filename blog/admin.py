from django.contrib import admin
from .models import Post # Use a . to indicate models file is in the same (working) directory

# Register your models here.
admin.site.register(Post)