from django.contrib.auth.models import BaseUserManager


class NewUserAccountManager(BaseUserManager):
    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault('admin', True)
        other_fields.setdefault("is_superuser", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        user = self.create_user(username, email, password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password, **other_fields):
        other_fields.setdefault("is_active", True)
        
        if not email:
            raise ValueError("Email address is required!")
        if not username:
            raise ValueError("Username is required!")
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
