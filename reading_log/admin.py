from django.contrib import admin
from .models import ReadingLog, Folder, UserReadingLog

# Register your models here.

admin.site.register(ReadingLog)
admin.site.register(Folder)
admin.site.register(UserReadingLog)