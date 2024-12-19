from django.contrib import admin # type: ignore
from .models import Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)
