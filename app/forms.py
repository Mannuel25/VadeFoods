from django import forms
from .models import Food, Proteins, Pastries, Drinks, Cart, Morsels


class FoodForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Food


class ProteinsForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Proteins


class PastriesForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Pastries


class DrinksForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Drinks


class MorselsForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Morsels


class CartForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Cart


class AllItemsForm(forms.Form):
    categories = (
        ('None', 'Select a Category'),
        ('food', 'Food'),
        ('proteins', 'Proteins'),
        ('pastries', 'Pastries'),
        ('drinks', 'Drinks'),
        ('morsels', 'Morsels'),
    )
    category = forms.ChoiceField(choices=categories)
    name = forms.CharField(label=("Enter the name"), max_length=225)
    price = forms.IntegerField(label=("Enter a price"), widget=forms.NumberInput)
    discounted_price = forms.IntegerField(label=("Enter a discounted price(optional)"), widget=forms.NumberInput, required=False)
    quantity = forms.IntegerField(label=("Enter the available quantity/portion"), widget=forms.NumberInput)
    item_folder = f"{category}_images/"
    image = forms.FileField()


