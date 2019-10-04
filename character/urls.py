from django.urls import path
from character import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.character, name='character'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
