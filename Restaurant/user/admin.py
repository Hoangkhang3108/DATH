from django.contrib import admin
from product.models import Product, Category, Variation
from cart.models import Cart, CartItem
from order.models import Order
from user.models import CustomerUser


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(CustomerUser)