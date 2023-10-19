from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from core.models import *
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    product = Main_category.objects.all()
    walpaper_cat = Company_name.objects.filter(wallpaper_category=True)
    curtain_sofa_brands = Company_name.objects.filter(curtain_sofa_brands=True)
    mattresses_brands = Company_name.objects.filter(mattresses_brands=True)
    window_blind_brands = Company_name.objects.filter(window_blinds_brands=True)
    carpet_tile_office = Company_name.objects.filter(carpet_tile_for_office_brands=True)
    rugs_brands = Company_name.objects.filter(rugs_brands=True)
    pillow_brands = Company_name.objects.filter(pillow_brands=True)
    hospital_floor_walls = Company_name.objects.filter(hospital_walls_brands=True)
    wooden_laminate = Company_name.objects.filter(wooden_laminate_flooring_brands=True)
    pvc_rubber = Company_name.objects.filter(pvc_rubber_flooring_brands=True)
    curtain_rods_channel = Company_name.objects.filter(curtains_rods_channel_brands=True)
    foam_material = Company_name.objects.filter(foam_material_brands=True)
    awning_canopy = Company_name.objects.filter(awning_canopy_brands=True)
    best_deal_prod = Product.objects.filter(best_deal=True)


    context = {
        "main_cat":product,
        "walpaper_cat": walpaper_cat,
        "curtain_sofa_brands": curtain_sofa_brands,
        "mattresses_brands": mattresses_brands,
        "window_blind_brands": window_blind_brands,
        "carpet_tile_office": carpet_tile_office,
        "rugs_brands": rugs_brands,
        "pillow_brands": pillow_brands,
        "hospital_floor_walls": hospital_floor_walls,
        "wooden_laminate": wooden_laminate,
        "pvcrubber": pvc_rubber,
        "curtain_rods_channel": curtain_rods_channel,
        "foam_material": foam_material,
        "awning_canopy": awning_canopy,
        "best_deal": best_deal_prod,
    }
    return render(request, 'core/index.html', context)

def category(request, cat_title):
    category = Category.objects.get(cat_title=cat_title)
    company_name =  Company_name.objects.filter(category=category)
    sub_category = Sub_categories.objects.filter(category=category)

    context = {
        "category": category,
        "company_name": company_name,
        "sub_category" : sub_category,
    }

    return render(request, "core/category.html", context)

def sub_category(request, sub_cat_title):
    sub_cat = get_object_or_404(Sub_categories, sub_cat_title=sub_cat_title)
    related_sub_categories = Sub_categories.objects.filter(maincat=sub_cat.maincat, category=sub_cat.category)
    company_names = Company_name.objects.filter(sub_category=sub_cat)
    
    # Create a dictionary to store company names and their associated products
    company_products = {}
    for company in company_names:
        products = Product.objects.filter(company_name=company)
        company_products[company] = products

    context = {
        "sub_cat": sub_cat,
        "company_products": company_products,
        "related_sub_categories": related_sub_categories,
    }

    return render(request, "core/sub-category.html", context)

def main_category(request, main_title):
    main_categories = Main_category.objects.get(main_title=main_title)
    categories = Category.objects.filter(main_category=main_categories)

    context = {
        "main_categories": main_categories,
        "categories": categories,
    }
    return render(request, "core/main_category.html", context)


def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product

    return JsonResponse({"data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})


def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            price_str = item['price'].replace('₹', '').replace(',', '').strip()
            price = float(price_str)
            cart_total_amount += int(item['qty']) * price

        return render(request, "core/cart.html", {"cart_data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    else:
        messages.warning(request, "Your cart is empty")
        return redirect("core:index")


def product(request, title):
    main_product = get_object_or_404(Product, title=title)
    related_products = Product.objects.filter(company_name=main_product.company_name).exclude(pk=main_product.pk)[:10]
    product_images = ProductImages.objects.filter(product=main_product)
    product_varients = ProductVarient.objects.filter(product=main_product)
    related_company = main_product.company_name
    related_subcategory = main_product.sub_category

    context = {
        "main_product": main_product,
        "related_products": related_products,
        "product_images": product_images,
        "related_company": related_company,
        "related_subcategory": related_subcategory,
        "product_varients" : product_varients,
    }
    return render(request, "core/product.html", context)


def search_view(request):
    query = request.GET.get("q")

    products = Product.objects.filter(title__icontains=query).order_by("-date")

    context = {
        "products": products,
        "query": query,
    }

    return render(request, "core/search.html", context)


def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
           cart_data = request.session['cart_data_obj']
           del request.session['cart_data_obj'][product_id]
           request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])


    context = render_to_string("core/cart.html", {"cart_data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})        



def update_cart(request):
    product_id = str(request.GET['id'])
    product_qty = request.GET['qty']
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
           cart_data = request.session['cart_data_obj']
           cart_data[str(request.GET['id'])]['qty'] = product_qty
           request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])


    context = render_to_string("core/cart.html", {"cart_data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])}) 



@login_required
def checkout_view(request):
    host = request.get_host()
    paypal_dict = {
        'business' : settings.PAYPAL_RECEIVER_EMAIL,
        'amount' : '200',
        'item_name' : "Order-item No. 3",
        'invoice' : "INVOICE_NO_3",
        'currency_code' : "INR",
        'notify_url' : 'http://{}{}'.format(host, reverse('core:paypal-ipn')),
        'return_url' : 'http://{}{}'.format(host, reverse('core:payment-completed')),
        'cancel_url' : 'http://{}{}'.format(host, reverse('core:payment-failed')),
    }

    paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)
     
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

    return render(request, "core/checkout.html", {"cart_data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount, 'paypal_payment_button': paypal_payment_button})

@login_required
def payment_completed_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
    return render(request, "core/payment-completed.html")

@login_required
def payment_failed_view(request):
    return render(request, "core/payment-failed.html")


def com_name(request):
    return render(request, "core/sub-category.html")



        
    





