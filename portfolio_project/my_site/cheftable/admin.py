from django.contrib import admin
from .models import Menus
from .models import MenuCategory
from .models import Logger


# Register your models here.
admin.site.register(Menus)
admin.site.register(MenuCategory)
admin.site.register(Logger)

