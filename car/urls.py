from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.ListCarView.as_view()), name="list"),
    path("create/", login_required(views.CreateCarView.as_view()), name="create"),
    path("update/<pk>/", login_required(views.UpdateCarView.as_view()), name="update"),
    path("detail/<pk>/", login_required(views.DetailCarView.as_view()), name="detail"),
    path("delete/<pk>/", login_required(views.DeleteCarView.as_view()), name="delete"),
    path("buy/<pk>/", views.BuyCarView, name="buy"),
    path("makeavailable/<pk>/", views.MakeAvailable, name="makeavailable"),
]
