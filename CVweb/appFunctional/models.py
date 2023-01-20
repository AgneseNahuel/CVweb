from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField


class modelPosteo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50, default='TEXTO EJEMPLO')
    Field = RichTextUploadingField(max_length=1000)
    Time = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.Title}'
