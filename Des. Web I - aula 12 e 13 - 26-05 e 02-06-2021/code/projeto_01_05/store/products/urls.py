from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<slug:slug>/", views.product_detail, name="product_detail"),
    path("category/<slug:slug>/", views.product_list, name="product_list_by_category"),
]