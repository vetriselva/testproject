from django.urls import path
from .views import index,update
urlpatterns = [
    path('estimate/', index, name= 'index'),
    path("update_server/", update, name="update"),
]