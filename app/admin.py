from django.contrib import admin
from .models import Food, Proteins, Pastries, Drinks, Cart


admin.site.register(Food)
admin.site.register(Proteins)
admin.site.register(Pastries)
admin.site.register(Drinks)
admin.site.register(Cart)
