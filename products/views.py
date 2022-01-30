from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Product
# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    context = {"name" : "justin"}
    return render(request, "home.html", context)


# def product_detail_view(request, *args, **kwargs):
#     obj = Product.objects.get(id = 1)
#     return HttpResponse(f"Product id {obj.id}")


def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id = id)
    except Product.DoesNotExist:
        raise Http404
        
    #return HttpResponse(f"Product id {obj.id}")
    return render(request, "products/detail.html", {"object":obj})


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list" : qs}
    return render(request, "products/list.html", context)