from django.urls import path
from character import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('/generate', views.character, name='character'),
        path('/download', views.download, name='download'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
