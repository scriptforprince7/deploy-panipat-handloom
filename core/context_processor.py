from core.models import *

def default(request):
    product = Main_category.objects.all()

    return {
        'main_cat': product,
    }