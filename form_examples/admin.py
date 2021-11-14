from django.contrib import admin

from form_examples.models import Message

# Register your models here.
# admin.site.register(Message)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "body")
