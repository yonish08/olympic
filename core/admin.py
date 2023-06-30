from django.contrib import admin
from core.models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.
class myModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(AboutFunOlympic)
admin.site.register(News)
admin.site.register(Country)
admin.site.register(Sport)
admin.site.register(Player)
admin.site.register(Highlight, myModelAdmin)
admin.site.register(LiveMatch)
admin.site.register(Fixture)
