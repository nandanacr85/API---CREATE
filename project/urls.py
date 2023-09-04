from django.urls import path

from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path(" detail/<int:id>",views.detial,name="detail")
]