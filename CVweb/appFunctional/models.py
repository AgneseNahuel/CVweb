from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model


class modelPosteoPython(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Title = models.CharField(max_length=50, default='TEXTO EJEMPLO')
    Field = RichTextUploadingField()
    Time = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.Title}'

class modelPosteoHTML(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Title = models.CharField(max_length=50, default='TEXTO EJEMPLO')
    Field = RichTextUploadingField()
    Time = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.Title}'

class modelPosteoCSS(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Title = models.CharField(max_length=50, default='TEXTO EJEMPLO')
    Field = RichTextUploadingField()
    Time = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.Title}'