from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dataentry/', include('dataentry.urls')),
    path('celery-test/', views.celery_test),
    # Registration and Login urls
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('emails/', include('emails.urls')),
    path('image-compression/', include('image_compression.urls')),
    path('webscarping/', include('stockanalysis.urls')),
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
