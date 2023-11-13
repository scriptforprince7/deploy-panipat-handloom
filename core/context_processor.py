from core.models import *

def default(request):
    product = Main_category.objects.all()

    return {
        'main_cat': product,
    }

def defaultOne(request):
    architectures = Architecture.objects.filter(featured=True)
    architecture = Architecture.objects.filter(featured=False)
    archi = Architecture.objects.all()

    return {
        "architectures": architectures,
        "architecture": architecture,
        "archi": archi,
    }
