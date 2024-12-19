from django.shortcuts import render, get_object_or_404 # type: ignore
from store.models import Product
from django.core.paginator import Paginator # type: ignore
from category.models import Category

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        product_count= products.count()
        paged_products = pagination (request, products, 4)
    else:
        products = Product.objects.all()
        product_count = products.count()
        paged_products = pagination (request, products, 4)
        
    return render(request, 'store.html', context= {
        'products': paged_products,
        'product_count': product_count,
    })
    
    
def pagination(request,products, products_by_page):
    paginator = Paginator(products, products_by_page)
    page = request.GET.get('page')
    page_products = paginator.get_page(page)
    return page_products

def product_detail(request, category_slug, product_slug):
    product = Product.objects.get(
        category__slug=category_slug, slug = product_slug)
    return render(request, 'product_detail.html', context= {'product': product})


def search(request):
    # q = parámetro de consulta
    query = request.GET.get('q', '')
    if query:
        results = Product.objects.filter(product_name__icontains=query)
    else:
        results = Product.objects.none() 

    return render(request, 'search_results.html', {'results': results, 'query': query})
