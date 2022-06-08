from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    subject = models.CharField(max_length=50, db_index=True)
    message = models.TextField(max_length=9999, db_index=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    replied = models.BooleanField(default=False)
