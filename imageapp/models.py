from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('travel', 'TRAVEL'),
    ('food', 'FOOD'),
    ('vehicle', 'VEHICLE'),
    ('landscape', 'LANDSCAPE'),
    ('potrait', 'POTRAIT'),

)


class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Image(models.Model):
    image_name = models.CharField(max_length=45)
    image_description = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='travel')
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_image(self):
        pass

    @classmethod 
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image

    @classmethod
    def search_image(cls, category_name):
        images = cls.objects.filter(category=category_name)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__name__icontains=location)
        return images

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images


class Comment(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def all_comments(cls, image_id):
        comments = cls.objects.filter(image=image_id)
        return comments
