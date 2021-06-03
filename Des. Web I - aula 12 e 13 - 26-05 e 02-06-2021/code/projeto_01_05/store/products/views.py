from django.db.models.manager import EmptyManager
from django.shortcuts import render, get_object_or_404
# from django.views.generic import DetailView, ListView

from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, **kwargs):
    category = None    
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    
    if kwargs:
        category = get_object_or_404(Category, slug = kwargs['slug'])
        products = products.filter(category=category)
    return render(request, 
        'products/product_list.html',
        {'category': category,
        'categories': categories,
        'product_list': products}
    )

def product_detail(request, **kwargs):
    product = get_object_or_404(Product, slug = kwargs['slug'], is_available=True)
    print(product.id)
    cart_product_form = CartAddProductForm()
    return render(request, 
        'products/product_detail.html', 
        {
            'product': product,
            'cart_product_form': cart_product_form
        }
    )
