from .views import *
from django.urls import path, include


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('purchase/', purchase_item, name='purchase'),
    path('generate_receipt/', generate_receipt, name='generate_receipt'),
    path('cart/', cart, name='cart'),
    path('cart/delete/<int:id>', delete_cart_items, name='delete_cart_items'),
    path('foods/', all_foods, name='foods'),
    path('food/edit/<int:id>', edit_food, name='edit_food'),
    path('food/delete/<int:id>', delete_food, name='delete_food'),
    path('items/add', add_items, name='add_items'),
    path('proteins/', all_proteins, name='proteins'),
    path('proteins/edit/<int:id>', edit_protein, name='edit_protein'),
    path('proteins/delete/<int:id>', delete_protein, name='delete_protein'),
    path('pastries/', all_pastries, name='pastries'),
    path('pastries/edit/<int:id>', edit_pastries, name='edit_pastries'),
    path('pastries/delete/<int:id>', delete_pastries, name='delete_pastries'),
    path('drinks/', all_drinks, name='drinks'),
    path('drinks/edit/<int:id>', edit_drink, name='edit_drink'),
    path('drinks/delete/<int:id>', delete_drink, name='delete_drink'),
    path('morsels/', all_morsels, name='morsels'),
    path('morsels/edit/<int:id>', edit_morsel, name='edit_morsel'),
    path('morsels/delete/<int:id>', delete_morsel, name='delete_morsel'),
]
