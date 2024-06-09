from django.contrib import admin
from .models import StreamModel,WatchModel,ReviewModel

admin.site.register((StreamModel,WatchModel,ReviewModel))