from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = RichTextField(max_length=9999, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
