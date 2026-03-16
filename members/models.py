from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"


class student(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


import uuid
from django.db import models

class Visitor(models.Model):

    visitor_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    referrer = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    consent_given = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.visitor_id)
    


import uuid
from django.db import models

class Visitors(models.Model):

    visitor_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    referrer = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    consent_given = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.visitor_id)    


from django.db import models

class Visitor2(models.Model):

    visitor_id = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)

    ip_address = models.GenericIPAddressField(null=True)
    user_agent = models.TextField()

    browser = models.CharField(max_length=50, null=True)
    os = models.CharField(max_length=50, null=True)
    device_type = models.CharField(max_length=20, null=True)

    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    screen_width = models.IntegerField(null=True)
    screen_height = models.IntegerField(null=True)

    language = models.CharField(max_length=20, null=True)
    timezone = models.CharField(max_length=50, null=True)

    page_url = models.TextField()
    page_title = models.TextField()
    referrer = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)            