from django.utils import timezone
from django.db import models


class MyImages(models.Model):
    myfile = models.FileField(upload_to='./uploaded_images/')
    title = models.CharField(max_length=50, blank=False, null=False)

    def __unicode__(self):
        return u"photo {0}".format(self.file.url)

