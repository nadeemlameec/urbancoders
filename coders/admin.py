from django.contrib import admin
from .models import Form
from .models import web
from .models import digi
from .models import graphic
# Register your models here.

admin.site.register(Form)
admin.site.register(web)
admin.site.register(digi)
admin.site.register(graphic)

