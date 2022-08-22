from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from statistic import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

