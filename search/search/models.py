from django.db import models
from search.utils import upload_image

class ImageTest(models.Model):
    testfield = models.CharField(max_length=20)
    image  = models.ImageField(editable=True, null=True)



