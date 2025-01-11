from django.contrib import admin
from.models import TBL_Usuario, TBL_Video, TBL_VideoUsuario

# Register your models here.

admin.site.register(TBL_Usuario)
admin.site.register(TBL_Video)
admin.site.register(TBL_VideoUsuario)