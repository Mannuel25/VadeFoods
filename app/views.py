from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
import random, time, datetime, string, io, os, requests
from app.models import Food, Proteins, Pastries, Drinks, Cart, Morsels, SoldFoodItems, CustomerReceipts
from app.forms import FoodForm, AllItemsForm, ProteinsForm, PastriesForm, DrinksForm, MorselsForm, CartForm
from users.models import CustomUser
from app.decorators import for_admins
from django.core.files.base import ContentFile
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import FileResponse

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

@login_required(login_url='login')
@for_admins
def add_items(request):
    if request.method == 'GET':
        form = AllItemsForm()
        return render(request, 'add_items.html', context={'form': form})
    elif request.method == 'POST':
        category = request.POST.get('category')
        # add inserted item to its respective category table
        if category == 'food':
            form = FoodForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif category == 'proteins':
            form = ProteinsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif category == 'pastries':
            form = PastriesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif category == 'drinks':
            form = DrinksForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif category == 'morsels':
            form = MorselsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        return redirect('add_items')

def all_proteins(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = Proteins.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            item = Cart.objects.get(name=item.name)
            item.no_of_orders += 1
            item.save()
        else:
            price = item.price if item.price else item.discounted_price
            Cart.objects.create(customer=user, name=item.name, price=price, image_name=item.image.name, category="proteins")
    if search_input:
        items = Proteins.objects.filter(name__icontains=search_input)
    else:
        items = Proteins.objects.all()
    context = {'items': items}
    return render(request, 'all_proteins.html', context)


@login_required(login_url='login')
@for_admins
def edit_protein(request, id):
    protein = get_object_or_404(Proteins, id=id)
    form = ProteinsForm(instance=protein)
    if request.method == 'POST':
        form = ProteinsForm(request.POST, request.FILES, instance=protein)
        if form.is_valid():
            form.save()
            return redirect('proteins')
    return render(request, 'edit_proteins.html', {'form': form, 'id': id})

@login_required(login_url='login')
@for_admins
def delete_protein(request, id):
    item = Proteins.objects.get(id=id)
    item.delete()
    return redirect('proteins')

def all_foods(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = Food.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            item = Cart.objects.get(name=item.name)
            item.no_of_orders += 1
            item.save()
        else:
            price = item.price if item.price else item.discounted_price
            Cart.objects.create(customer=user, name=item.name, price=price, image_name=item.image.name, category="food")
    else:
        items = Food.objects.all()
    if search_input:
        items = Food.objects.filter(name__icontains=search_input)
    else:
        items = Food.objects.all()
    context = {'items': items}
    return render(request, 'all_foods.html', context)

@login_required(login_url='login')
@for_admins
def edit_food(request, id):
    item = get_object_or_404(Food, id=id)
    form = FoodForm(instance=item)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('foods')
    return render(request, 'edit_food.html', {'form': form, 'id': id})

@login_required(login_url='login')
@for_admins
def delete_food(request, id):
    item = Food.objects.get(id=id)
    item.delete()
    return redirect('foods')

def all_pastries(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = Pastries.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            item = Cart.objects.get(name=item.name)
            item.no_of_orders += 1
            item.save()
        else:
            price = item.price if item.price else item.discounted_price
            Cart.objects.create(customer=user, name=item.name, price=price, image_name=item.image.name, category="pastries")
    if search_input:
        items = Pastries.objects.filter(name__icontains=search_input)
    else:
        items = Pastries.objects.all()
    context = {'items': items}
    return render(request, 'all_pastries.html', context)

@login_required(login_url='login')
@for_admins
def edit_pastries(request, id):
    item = get_object_or_404(Pastries, id=id)
    form = PastriesForm(instance=item)
    if request.method == 'POST':
        form = PastriesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('pastries')
    return render(request, 'edit_pastries.html', {'form': form, 'id': id})

@login_required(login_url='login')
@for_admins
def delete_pastries(request, id):
    item = Pastries.objects.get(id=id)
    item.delete()
    return redirect('pasteries')

def all_drinks(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = Drinks.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            item = Cart.objects.get(name=item.name)
            item.no_of_orders += 1
            item.save()
        else:
            price = item.price if item.price else item.discounted_price
            Cart.objects.create(customer=user, name=item.name, price=price, image_name=item.image.name, category="drinks")
    if search_input:
        items = Drinks.objects.filter(name__icontains=search_input)
    else:
        items = Drinks.objects.all()
    context = {'items': items}
    return render(request, 'all_drinks.html', context)

@login_required(login_url='login')
@for_admins
def edit_drink(request, id):
    item = get_object_or_404(Drinks, id=id)
    form = DrinksForm(instance=item)
    if request.method == 'POST':
        form = DrinksForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('drinks')
    return render(request, 'edit_drinks.html', {'form': form, 'id': id})

@login_required(login_url='login')
@for_admins
def delete_drink(request, id):
    item = Drinks.objects.get(id=id)
    item.delete()
    return redirect('drinks')

def all_morsels(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = Morsels.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            item = Cart.objects.get(name=item.name)
            item.no_of_orders += 1
            item.save()
        else:
            price = item.price if item.price else item.discounted_price
            Cart.objects.create(customer=user, name=item.name, price=price, image_name=item.image.name, category="morsels")
    if search_input:
        items = Morsels.objects.filter(name__icontains=search_input)
    else:
        items = Morsels.objects.all()
    context = {'items': items}
    return render(request, 'all_morsels.html', context)

@login_required(login_url='login')
@for_admins
def edit_morsel(request, id):
    item = get_object_or_404(Morsels, id=id)
    form = MorselsForm(instance=item)
    if request.method == 'POST':
        form = MorselsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('morsels')
    return render(request, 'edit_morsel.html', {'form': form, 'id': id})

@login_required(login_url='login')
@for_admins
def delete_morsel(request, id):
    item = Morsels.objects.get(id=id)
    item.delete()
    return redirect('morsels')

def calc_item_total_amout(item):
    """calculates the amount an items costs per no of orders"""
    total = item.no_of_orders * item.price
    item.total_amount = f"{total:,d}"

def get_cart_total_amount(customer):
    """calculates the total amount all items in cart costs"""
    cart_total_amount = 0
    for item in Cart.objects.filter(customer=customer):
        total_price = item.price * item.no_of_orders
        cart_total_amount += total_price
    return f"{cart_total_amount:,d}"

@login_required(login_url='login')
def cart(request):
    get_red_quan, get_inc_quan = request.GET.get('reduce_quantity'), request.GET.get('increase_quantity')
    search_input = request.GET.get('search_input')
    user = CustomUser.objects.get(username=request.user.username)
    if get_red_quan:
        item = Cart.objects.get(customer=user, name=get_red_quan)
        item.no_of_orders -= 1
        calc_item_total_amout(item)
        item.delete() if item.no_of_orders == 0 else item.save()
    if get_inc_quan:
        item = Cart.objects.get(customer=user, name=get_inc_quan)
        item.no_of_orders += 1
        calc_item_total_amout(item)
        item.save()
    cart_total_amount = get_cart_total_amount(request.user)
    if search_input:
        cart = Cart.objects.filter(name__icontains=search_input)
    else:
        cart = Cart.objects.all()
    context = {'cart': cart, 'cart_total_amount': cart_total_amount}
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def delete_cart_items(request, id):
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('cart')

@login_required(login_url='login')
@for_admins
def inventory(request):
    if request.method == 'GET':
        all_food_items = SoldFoodItems.objects.filter(category="food")
        all_proteins_items = SoldFoodItems.objects.filter(category="proteins")
        all_drinks_items = SoldFoodItems.objects.filter(category="drinks")
        all_pastries_items = SoldFoodItems.objects.filter(category="pastries")
        all_morsels_items = SoldFoodItems.objects.filter(category="morsels")

        popular_food = all_food_items.order_by('-no_of_orders')[0] if len(all_food_items) > 0 else all_food_items
        least_popular_food = all_food_items.order_by('no_of_orders')[0] if len(all_food_items) > 0 else all_food_items
        if popular_food == least_popular_food:
            popular_food, least_popular_food = None, None

        popular_protein = all_proteins_items.order_by('-no_of_orders')[0] if len(all_proteins_items) > 0 else all_proteins_items
        least_popular_protein = all_proteins_items.order_by('no_of_orders')[0] if len(all_proteins_items) > 0 else all_proteins_items
        if popular_protein == least_popular_protein:
            popular_protein, least_popular_protein = None, None

        popular_drink = all_drinks_items.order_by('-no_of_orders')[0] if len(all_drinks_items) > 0 else all_drinks_items
        least_popular_drink = all_drinks_items.order_by('no_of_orders')[0] if len(all_drinks_items) > 0 else all_drinks_items
        if popular_drink == least_popular_drink:
            popular_drink, least_popular_drink = None, None

        popular_pastry = all_pastries_items.order_by('-no_of_orders')[0] if len(all_pastries_items) > 0 else all_pastries_items
        least_popular_pastry = all_pastries_items.order_by('no_of_orders')[0] if len(all_pastries_items) > 0 else all_pastries_items
        if popular_pastry == least_popular_pastry:
            popular_pastry, least_popular_pastry = None, None

        popular_morsel = all_morsels_items.order_by('-no_of_orders')[0] if len(all_morsels_items) > 0 else all_morsels_items
        least_popular_morsel = all_morsels_items.order_by('no_of_orders')[0] if len(all_morsels_items) > 0 else all_morsels_items
        if popular_morsel == least_popular_morsel:
            popular_morsel, least_popular_morsel = None, None

        search_input = request.GET.get('search_input')
        if search_input:
            items = SoldFoodItems.objects.filter(food_name__icontains=search_input)
            if items:
                items_cat = items.first().category
            else:
                items, items_cat = {}, None
        else:
            items, items_cat = {}, None

        context = {
            'popular_food': popular_food,
            'popular_protein' : popular_protein,
            'popular_drink' : popular_drink,
            'popular_pastry' : popular_pastry,
            'popular_morsel' : popular_morsel,
            'least_popular_food': least_popular_food,
            'least_popular_protein' : least_popular_protein,
            'least_popular_drink' : least_popular_drink,
            'least_popular_pastry' : least_popular_pastry,
            'least_popular_morsel' : least_popular_morsel,
            'items' : items,
            'item_category' : items_cat,
        }
        return render(request, 'inventory.html', context)

def purchase_item(request):
    for item in Cart.objects.filter(customer=request.user):
        if item.category == 'food':
            food = Food.objects.get(name=item.name)
        elif item.category == 'proteins':
            food = Proteins.objects.get(name=item.name)
        elif item.category == 'pastries':
            food = Pastries.objects.get(name=item.name)
        elif item.category == 'drinks':
            food = Drinks.objects.get(name=item.name)
        elif item.category == 'morsels':
            food = Morsels.objects.get(name=item.name)
        # reduce the quantiy available after purchase
        food.quantity -= item.no_of_orders
        food.save()

        # save the bought food items to db
        # check if that food item has been bought before
        food_item = SoldFoodItems.objects.filter(name=food.name)
        if food_item.exists():
            # re-calculate the number of orders and amount made
            food_item = food_item.first()
            food_item.no_of_orders += item.no_of_orders
            total_amount = food_item.price  * food_item.no_of_orders
            food_item.total_amount = f"{total_amount:,d}"
            food_item.save()
        else:
            data = {
                "customer" : item.customer,
                "name" : item.name,
                "price" : item.price,
                "no_of_orders" : item.no_of_orders,
                "category" : item.category,
                "image_name" : item.image_name,
                "total_amount" : item.total_amount
            }
            SoldFoodItems.objects.create(**data)
    # generate receipt
    items = Cart.objects.filter(customer=request.user)
    receipt = CustomerReceipts.objects.filter(customer=request.user)
    if receipt.exists():
        receipt.delete()
    file_path = generate_receipt(request.user, items)
    time.sleep(0.5)
    # delete items in cart after purchase
    items.delete()
    return FileResponse(open(f"media/{file_path}", 'rb'), content_type="application/pdf")
    # return redirect("cart")

def generate_receipt(customer, items):
    try:
        template = get_template('generate_receipt.html')
        # format the date, time to be used in the pdf
        current_date_time = datetime.datetime.now()
        formatted_time = current_date_time.time().strftime("%H:%M:%S")
        formatted_date = current_date_time.strftime("%A %dth %B, %Y")
        # generate a random invoice number
        random_number = str(datetime.datetime.now().timestamp()).replace(".", "")
        chars = list(string.ascii_uppercase)
        random.shuffle(chars)
        invoice_number = f"{random_number[:7]}-{''.join(i for i in chars[:3])}{random_number[8:10]}-{random_number[11:14]}"
        cart_total_amount = get_cart_total_amount(customer)
        data = {
            "name": customer.username.title(),
            "items": items,
            "today_date": formatted_date,
            "time_generated": formatted_time,
            "invoice_number": invoice_number,
            "cart_total_amount": cart_total_amount
        }

        html = template.render(data)
        result = io.BytesIO()
        pisa_context = pisa.CreatePDF(html, result)
        if pisa_context.err:
            print(str(pisa_context.err))
            raise ValueError("Unexpected value for pisaContext")
        else:
            # generate random file number
            number = random.randint(1000, 9999)
            filename = f'VadeFoods-{number}-receipt.pdf'
            with open(filename, 'wb') as f:
                file = f.write(result.getvalue())
            with open(filename, 'rb') as f:
                pdf_bytes = f.read()
            customer_receipt = CustomerReceipts.objects.create(customer=customer, invoice_number=invoice_number)
            pdf = ContentFile(pdf_bytes)
            customer_receipt.receipt.save(filename, pdf) 
            customer_receipt.save()
            os.remove(filename)
            return customer_receipt.receipt.name
    except Exception as e:
        print(str(e))
        raise ValueError("Unexpected value for pisaContext")

