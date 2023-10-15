from django.contrib import admin
from core.models import *

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductVariantImagesAdmin(admin.TabularInline):
    model = ProductVariantImages
    extra = 1  # This allows adding multiple images at once in the admin

class ProductVarientAdmin(admin.TabularInline):
    model = ProductVarient
    inlines = [ProductVariantImagesAdmin]


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin, ProductVarientAdmin, ProductVariantImagesAdmin]
    list_display = ['company_name', 'main_category', 'category', 'sub_category', 'title', 'price', 'featured', 'product_status']
    list_filter = ['company_name', 'main_category', 'category', 'sub_category', 'featured', 'product_status']  # Add fields you want to filter by
    search_fields = ['title', 'description']  # Add fields you want to search by


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['main_title', 'meta_description', 'meta_title', 'meta_tag', 'image', 'icon_img']     

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['main_category', 'cat_title', 'meta_description', 'meta_title', 'meta_tag', 'image', 'big_image']
    list_filter = ['main_category']  # Fields to filter by

class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ['maincat', 'category', 'sub_category', 'company_name_title', 'user', 'meta_description', 'meta_title', 'meta_tag', 'image', 'logo_img']
    list_filter = ['maincat', 'category', 'sub_category']  # Add fields you want to filter by
    search_fields = ['company_name_title', 'meta_description', 'meta_title', 'meta_tag']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['maincat', 'category', 'sub_cat_title', 'user', 'meta_description', 'meta_title', 'meta_tag', 'image']
    list_filter = ['maincat', 'category']  # Add fields you want to filter by
    search_fields = ['sub_cat_title', 'meta_description', 'meta_title', 'meta_tag']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating'] 

class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']              

admin.site.register(Product, ProductAdmin)
admin.site.register(Main_category, MainCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company_name, CompanyNameAdmin)
admin.site.register(Sub_categories, SubCategoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, wishlistAdmin)
admin.site.register(Address, AddressAdmin)

    


