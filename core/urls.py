from django.urls import include, path
from core.views import *

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    # path("<cat_title>/", category, name="category"),
    path("category/<cat_title>/", category, name="inner-category"),
    path("sub-category/<sub_cat_title>/", sub_category, name="sub-category"),
    path("shop-category/<main_title>/", main_category, name="main_category"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("cart/", cart_view, name="cart"),
    path("product/<title>/", product, name="product"),
    path("search/", search_view, name="search"),
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
    path("update-cart/", update_cart, name="update-cart"),
    path("checkout/", checkout_view, name="checkout"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path("payment-completed/", payment_completed_view, name="payment-completed"),
    path("payment-failed/", payment_failed_view, name="payment-failed"),
]
