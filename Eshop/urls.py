from django.contrib import admin
from django.urls import path, include
from Eshop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('base.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('store/', include('store.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
