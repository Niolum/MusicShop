from musicshop.api.cart.urls import cart_urlpatterns
from musicshop.api.product.urls import product_urlpatterns
from musicshop.api.user.urls import user_urlpatterns


urlpatterns = []
urlpatterns += cart_urlpatterns
urlpatterns += product_urlpatterns
urlpatterns += user_urlpatterns


