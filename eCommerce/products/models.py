from django.db import models
import random
import os
from django.db.models.signals import pre_save, post_save
from products.utils import unique_slug_generator
from django.urls import reverse


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(filepath)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 20000)
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f'products/{new_filename}/{final_filename}'


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    discription = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null="True", blank=True)
    feature = models.BooleanField(default="False")
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_path(self):
        # return f"/products/{self.slug}/"
        return reverse('products:detail', kwargs=dict(
            slug = self.slug
        ))

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, Product)
