from django.contrib import admin
from .models import Comments, Crops, Deeplearnings, Dronerunnings, Farmdiaries, Pestinfos, Ptcinfos, Users

# Register your models here.

admin.site.register(Comments)
admin.site.register(Crops)
admin.site.register(Deeplearnings)
admin.site.register(Dronerunnings)
admin.site.register(Farmdiaries)
admin.site.register(Pestinfos)
admin.site.register(Ptcinfos)
admin.site.register(Users)
