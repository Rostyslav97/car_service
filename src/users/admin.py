from django.contrib import admin
from users. models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("phone_number", "fullname", "car", "last_login")
    exclude = ("user_permissions", "groups", "password") 