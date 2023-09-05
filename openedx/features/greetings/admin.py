from django.contrib import admin
from openedx.features.greetings.models import Greeting


class GreetingAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', )


admin.site.register(Greeting, GreetingAdmin)
