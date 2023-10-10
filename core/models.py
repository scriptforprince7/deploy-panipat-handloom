from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from unicodedata import decimal
from pyexpat import model
from email.policy import default


STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING = (
    ("1", "★"),
    ("2", "★★"),
    ("3", "★★★"),
    ("4", "★★★★"),
    ("5", "★★★★★"),
)

COLOR = (
    ("red", "Red"),
    ("black", "Black"),
    ("pink", "Pink"),
    ("blue", "Blue"),
    ("orange", "Orange"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Main_category(models.Model):
    mid = ShortUUIDField(unique=True, max_length=30, prefix="main_cat", alphabet="abcdefgh12345")
    main_title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category",default="maincategory.jpg")
    icon_img = models.ImageField(upload_to="categoryicon",default="maincategoryicon.jpg")

    class Meta:
        verbose_name_plural = "Main Categories"

    def main_category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def main_category_icon_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.icon_img.url))
    
    def __str__(self):
        return self.main_title
    
class Category(models.Model):
    cid = ShortUUIDField(unique=True, max_length=30, prefix="cat", alphabet="abcdefgh12345")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    main_category = models.ForeignKey(Main_category, on_delete=models.SET_NULL, null=True)
    cat_title = models.CharField(max_length=100, default="Mobile & Laptop")
    meta_description = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, default="category.jpg")
    big_image = models.ImageField(upload_to=user_directory_path, default="bigcategory.jpg")


    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def category_big_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.big_image.url))
    
    def __str__(self):
        return self.cat_title
    

class Tags(models.Model):
    pass    

class Sub_categories(models.Model):
    ssid = ShortUUIDField(unique=True, max_length=30, prefix="sub_cat", alphabet="abcdefgh12345")   
    maincat = models.ForeignKey(Main_category, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sub_cat_title = models.CharField(max_length=100, default="Mobile & Laptop")
    meta_description = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_tag = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, default="subcategory.jpg")
    main_page_img = models.ImageField(upload_to=user_directory_path, default="mainpageimg.jpg")

    class Meta:
        verbose_name_plural = "Sub Categories"

    def sub_category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def main_page_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.main_page_img.url))
    
    def __str__(self):
        return self.sub_cat_title
    
class Company_name(models.Model):
    sid = ShortUUIDField(unique=True, max_length=50, prefix="Company_name", alphabet="abcdefgh12345")   
    maincat = models.ForeignKey(Main_category, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(Sub_categories, on_delete=models.SET_NULL, null=True)
    company_name_title = models.CharField(max_length=100, default="Mobile & Laptop")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    meta_description = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_tag = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    best_seller = models.BooleanField(default=False)
    curtain_fabric_category = models.BooleanField(default=False)
    fabric_use_upholstery_category = models.BooleanField(default=False)
    window_blinds_category = models.BooleanField(default=False)
    wall_panel_category = models.BooleanField(default=False)
    wallpaper_category = models.BooleanField(default=False)
    curtain_sofa_brands = models.BooleanField(default=False)
    mattresses_brands = models.BooleanField(default=False)
    window_blinds_brands = models.BooleanField(default=False)
    carpet_tile_for_office_brands = models.BooleanField(default=False)
    carpet_rolls_brands = models.BooleanField(default=False)
    rugs_brands = models.BooleanField(default=False)
    hospital_walls_brands = models.BooleanField(default=False)
    wooden_laminate_flooring_brands = models.BooleanField(default=False)
    curtains_rods_channel_brands = models.BooleanField(default=False)
    foam_material_brands = models.BooleanField(default=False)
    awning_canopy_brands = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_directory_path, default="subcategory.jpg")
    main_page_img = models.ImageField(upload_to=user_directory_path, default="mainpageimg.jpg")
    logo_img = models.ImageField(upload_to=user_directory_path, default="logo.jpg")

    class Meta:
        verbose_name_plural = "Company Name"

    def sub_category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def main_page_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.main_page_img.url))
    
    def logo_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo_img.url))
    
    def __str__(self):
        return self.company_name_title
    

class Product(models.Model):
    pid = ShortUUIDField(unique=True, max_length=30, prefix="sub_cat", alphabet="abcdefgh12345")
    main_category = models.ForeignKey(Main_category, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(Sub_categories, on_delete=models.SET_NULL, null=True)
    company_name = models.ForeignKey(Company_name, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="Mobile & Laptop")
    meta_description = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    meta_tag = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, default="This is the product")
    price = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=99999999999, decimal_places=2, default="2.99")
    discount_for_user = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")
    discount_for_architect = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")
    discount_for_importers = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")
    specifications = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    color = models.CharField(choices=COLOR, max_length=10, default="black")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    best_deal = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    sku = ShortUUIDField(unique=True, max_length=50, prefix="sku", alphabet="12345678900")
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")

    class Meta:
        verbose_name_plural = "Product"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Product Images"



class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    class Meta:
        verbose_name_plural = "Cart Order"



class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")

    class Meta:
        verbose_name_plural = "Cart Order Items"


    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image.url))   



class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return self.product.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"

        


    






    

    
