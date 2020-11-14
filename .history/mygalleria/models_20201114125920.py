from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
  image = CloudinaryField('image')

class Category(models.Model):
    category = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.category
    # def save_category(self):
    #     self.save()
    # def delete_category(self):
    #     self.delete()
    # @classmethod
    # def update(cls,id,name):
    #     category = Category.objects.filter(id=id)
    #     category.update(category=name)