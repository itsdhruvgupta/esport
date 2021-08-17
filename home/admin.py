from django.contrib import admin
from home.models import registration , event, winners, banner

# Register your models here.
admin.site.register(registration)

admin.site.register(event)

admin.site.register(winners)

admin.site.register(banner)