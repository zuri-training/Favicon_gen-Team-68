from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from .utils import file_path


class NewUserAccountManager(BaseUserManager):
    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        user = self.create_user(username, email, password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password, **other_fields):
        if not email:
            raise ValueError("Email address is required!")
        email = self.normalize_email(email)
        if password is not None:
            user = self.model(
                username=username,
                email=email,
                password=password,
                **other_fields,
            )
            user.save()
        else:
            user = self.model(
                username=username,
                email=email,
                password=password,
                **other_fields,
            )
            user.set_unusable_password()
            user.save()

        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = NewUserAccountManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username"]


# The foreignKey is not what we want
class Icon(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=file_path)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"], name="unique_icon_per_user"
            ),
        ]


class Result(models.Model):
    """
    I figured out that we only need on upload per result.
    We will populate the 'zip_file' field in the view by using the upload field
    """

    name = models.CharField(max_length=100)
    upload = models.OneToOneField(Icon, on_delete=models.CASCADE)
    zip_file = models.FileField(upload_to=file_path)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created", "name"]
