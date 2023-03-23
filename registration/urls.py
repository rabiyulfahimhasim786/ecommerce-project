from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from user import views as user_views

admin.site.site_header="SAASKIN ADMIN"
from registration import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('search/', user_views.search, name='search'),
    path('filter_by_category/', user_views.filter_by_category, name='filter_by_category'),
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)