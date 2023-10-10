from django.contrib import admin
from userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'email_verified', 'phone_number']
    readonly_fields = ['password', 'email']


admin.site.register(User, UserAdmin)
