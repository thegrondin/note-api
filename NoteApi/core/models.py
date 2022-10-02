from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email Address",
        max_length=255,
        unique=True,
    )

    firstname = models.CharField(
        verbose_name="Firstname",
        max_length=255,
    )

    lastname = models.CharField(
        verbose_name="Lastname",
        max_length=255
    )

    def __str__(self):
        return "Identifier : %s - Fullname: %s %s" % (self.email, self.firstname, self.lastname)


class Note(models.Model):

    date_created = models.DateTimeField(
        auto_now=True
    )

    title = models.CharField(
        verbose_name="Note Title",
        max_length="255"
    )

    content = models.TextField(
        verbose_name="Note Content"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Title: %s - Date created : %s" % (self.title, self.date_created)

    class Meta:
        ordering = ['date_created']


