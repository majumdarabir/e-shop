from django.contrib import admin
from django.urls import path, include
from Eshop import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('base.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "DJANGO_MEDIC_SHOP".title()
