from django.db import models
from cloudinary.models import CloudinaryField as BaseCloudinaryField
from django.contrib.auth.models import User


class CloudinaryField(BaseCloudinaryField):
    def upload_options(self, model_instance):
        return {
            'public_id': model_instance.name,
            'filename': Code.Author.Name,
            'unique_filename': False,
            'overwrite': False,
            'resource_type': 'auto',
            'tags': ['Sales'],
            'invalidate': True,
            'quality': 'auto:eco',
        }


# Create your models here.
class UserProf(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    RollNo = models.IntegerField(default=69)
    Name = models.CharField(default="Name", max_length=250)
    Profile_pic = CloudinaryField('Profile_Pic', overwrite=True)

    def __str__(self):
        return f"{self.User.username}-{self.Name}"


class CodeProb(models.Model):
    Writer = models.ForeignKey(UserProf, on_delete=models.CASCADE)
    Title = models.CharField(default="Title", max_length=200)
    Problem = models.TextField(default="Hello World")

    def __str__(self):
        return f"{self.Title}-{self.Writer.Name}"


class Status(models.Model):
    Prblm = models.ForeignKey(CodeProb, on_delete=models.CASCADE, default=1)
    UserAsg = models.ForeignKey(UserProf, on_delete=models.CASCADE, default=1)
    Sts = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Prblm.Title}-{self.UserAsg}"


class Code(models.Model):
    Author = models.ForeignKey(UserProf, default=1, on_delete=models.CASCADE)
    Problem = models.ForeignKey(CodeProb, default=1, on_delete=models.CASCADE)
    ScrSht = CloudinaryField('Screen Shot')

    def __str__(self):
        return f"{self.Problem.Title}-{self.Author.Name}"
