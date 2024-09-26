from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('sno', 'name', 'email', 'phone', 'content', 'timeStamp')

admin.site.register(Contact, ContactAdmin)