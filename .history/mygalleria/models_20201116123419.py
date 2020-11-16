from django.db import models
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    image = CloudinaryField('image')


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update(cls, id, name):
        category = Category.objects.filter(id=id)
        category.update(category=name)


class Location(models.Model):
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.place

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update(cls, id, name):
        place = Location.objects.filter(id=id)
        place.update(place=name)


class mygalleria_image(models.Model):
    image = CloudinaryField('image', default="./media")
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @classmethod
    def display_photo(cls):
        photo = cls.objects.all()
        return photo

    def save_image(self):
        self.save()

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_term):
        image = cls.objects.filter(
            category_id__category__icontains=search_term)
        return image

    @classmethod
    def update(cls, id, name):
        image = mygalleria_image.objects.filter(id=id)
        image.update(name=name)
        return image

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = mygalleria_image.objects.get(id=id)
        return image

    @classmethod
    def filter_location(cls, fil):
        location_image = mygalleria_image.objects.filter(
            location__place__icointain=fil)
        return location_image
