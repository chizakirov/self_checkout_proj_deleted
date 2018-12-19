from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'upload$', views.upload_file),
    url(r'read$', views.read_barcode),
    url(r'scanner$', views.scanner),
]
