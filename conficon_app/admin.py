from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileChangeForm, ProfileCreationForm
from .models import Icon, Profile, Result


class ImageInline(admin.TabularInline):
    model = Icon
    extra = 0


class ProfileAdmin(UserAdmin):
    inlines = (ImageInline,)
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ["username", "email"]
    fieldsets = (
        ("Auth", 
            {"fields": ("username", "email", "password")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Icon)
admin.site.register(Result)
