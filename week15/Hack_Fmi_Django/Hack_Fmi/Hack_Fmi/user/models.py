from django.db import models
from django.http import HttpResponse

# Create your models here.

from Hack_Fmi.lectures.models import Lecture
from Hack_Fmi.courses.models import Course
from Hack_Fmi.decorators import encrypt_pass, pbkdf2_sha256


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    edit_lecture = models.BooleanField(default=False)

    @classmethod
    def exists(cls, email):
        try:
            User.objects.filter(email=email)
            return True
        except User.DoesNotExist:
            return False

    # @encrypt_pass
    @classmethod
    def user_login(cls, email=None, password=None):
        try:
            # import ipdb; ipdb.set_trace()
            usr = cls.objects.get(email=email)
            if pbkdf2_sha256.verify(password, usr.password):
                return usr
            return False
        except cls.DoesNotExist:
            return False



# >>> # verifying the password
# >>> pbkdf2_sha256.verify("toomanysecrets", hash)
# True
# >>> pbkdf2_sha256.verify("joshua", hash)
# False


class Student(User):
    attending = models.ManyToManyField(Course)


class Tutor(User):
    lecturing = models.ManyToManyField(Lecture)
