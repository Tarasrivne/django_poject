from django.db import models

# class Drinks(models.Model):
#     drink_name = models.CharField(max_length=200)
#     price = models.IntegerField
# class MenuCategory(models.Model):
#     menu_category_name = models.CharField(max_length=200)
#
# class Menu(models.Model):
#     menu_item = models.CharField(max_length=200)
#     price = models.IntegerField(null=False)
#     category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)



class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # shift = forms.ChoiceField(choices=SHIFTS)
    time_log = models.TimeField(help_text=" Введіть якийсь час може?!!")

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField

    def __str__(self) -> str:
        return self.first_name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField

    def __str__(self) -> str:
        return self.name