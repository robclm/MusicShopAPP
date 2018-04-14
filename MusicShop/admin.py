# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Artist)
admin.site.register(Label)
admin.site.register(Release)
admin.site.register(ReleaseGroup)
admin.site.register(Recording)
admin.site.register(Work)