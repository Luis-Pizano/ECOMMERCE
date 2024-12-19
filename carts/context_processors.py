from .models import Cart, CartItem
from .views import cart_id

def counter_items(request):
    cart_count = 0
    
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            cart_count += cart_item.quantity
    except Cart.DoesNotExist:  
        cart_count = 0
    
    
    return {'cart_count': cart_count}



def total_products(request):
    total_products = 0
    try:
        cart = Cart.objects.get(cart_id=request.session.session_key)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        total_products = sum(item.quantity for item in cart_items)
    except Cart.DoesNotExist:
        print("no products in the cart")

    return {'total_products': total_products}
