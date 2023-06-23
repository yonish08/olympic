from django.contrib import admin
from user.models import Customer, SiteAdmin

# Register your models here.
admin.site.register(Customer)
admin.site.register(SiteAdmin)