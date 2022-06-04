from django.urls import path
from cart.views.views import (
    CartView, 
    AddToCartView, 
    DeleteFromCartView, 
    ChangeQTYView, 
    OrderCheckView, 
    MakeOrderView,
    AddWishlist,
    WishlistView,
    DeleteFromWishlist
)



urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:url>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:url>', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:url>', ChangeQTYView.as_view(), name='change_qty'),
    path('ordercheck/', OrderCheckView.as_view(), name='ordercheck'),
    path('makeorder/', MakeOrderView.as_view(), name='makeorder'),
    path('add-wishlist/<slug:slug>/', AddWishlist.as_view(), name='add_wishlist'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('delete-from-wishlist/<slug:slug>/', DeleteFromWishlist.as_view(), name='delete_from_wishlist')
]