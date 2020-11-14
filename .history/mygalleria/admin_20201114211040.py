from django.contrib import admin
from .models import Category,Image,Location,Photo

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(mygalleria_image)
admin.site.register(Photo)