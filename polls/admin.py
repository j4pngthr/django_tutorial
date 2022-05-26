from django.contrib import admin

# Register your models here.
from .models import Question

# adminページにpollsアプリを
admin.site.register(Question)
