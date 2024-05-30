from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),  # Assuming this is for products
    path('contact/', views.contact, name='contact'), # Added a trailing slash to 'contact'
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
