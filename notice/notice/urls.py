from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import faq.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', faq.views.home, name='home'),
    path('faq/', include('faq.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
