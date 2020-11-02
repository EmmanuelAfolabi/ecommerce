from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('cart', views.cart, name='cart'),
    path('product/<int:pk>/', views.detail, name='product'),
    path('secondindex', views.secondindex, name='secondindex'),
    path('checkout', views.checkout, name='checkout'),
    path('update_item', views.updateItem, name='update_item'),
    path('process_order', views.processOrder, name='process_order'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('login', views.user_log, name='login'),
    path('subscriber', views.subscriber, name='subscriber'),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)