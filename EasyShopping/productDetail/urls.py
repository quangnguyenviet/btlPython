from django.urls import path
from . import views
urlpatterns = [
    path('products/<int:id>/', views.ProductDetailView.as_view()),
]
