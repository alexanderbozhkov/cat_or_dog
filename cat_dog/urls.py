from django.urls import path
from django.conf.urls import url
from cat_dog.views import MyUploadView


urlpatterns = [
    url(r'^images/upload/$', MyUploadView.as_view()),
]