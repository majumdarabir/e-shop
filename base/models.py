from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile


def some_time():
    current_datetime: datetime = timezone.now()
    return timezone.datetime(year=current_datetime.year-5, month=1, day=1)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(default=some_time)
    image = models.ImageField(
        upload_to="profile", default="defaults/user.png")

    def __str__(self) -> str:
        return f"{self.user}"

    def save(self, *args, **kwags) -> None:
        if self.image:
            self.resize_photo(self.image)
        return super().save(*args, **kwags)

    def resize_photo(self, photo):
        img = Image.open(photo).convert("RGB")
        if img.size > (512, 512):
            img.thumbnail((512, 512))
        output = BytesIO()
        # Save resize image to bytes
        img.save(output, format="JPEG")
        output.seek(0)
        # Read output and create ContentFile in memory
        content_file = ContentFile(output.read())
        file = File(content_file)
        # get only the name of the photo
        photo.save(f"{photo.name}", file, save=False)

 # implementation of profile change
