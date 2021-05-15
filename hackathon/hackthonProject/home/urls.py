from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

urlpatterns = [
    path( "", views.index, name='home' ),
    path( "about", views.about, name='about' ),
    path( "services", views.services, name='services' ),
    path( "contact", views.contact, name='contact' ),
    path( "diagnosis", views.diagnosis, name='diagnosis' ),
    path("upload", views.image_upload_view,name='chalja'),
    path("output", views.checkView,name='check')
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)