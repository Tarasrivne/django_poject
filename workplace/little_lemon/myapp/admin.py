from django.contrib import admin
# from .models import Menu
# from .models import MenuCategory
from .models import Logger
from .models import Employees
from .models import Menu

admin.site.register(Logger)
# admin.site.register(Menu)
# admin.site.register(MenuCategory)

# Register your models here.
admin.site.register(Employees)
admin.site.register(Menu)