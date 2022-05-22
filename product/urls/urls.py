from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from product.views.views import (
    CategoryListView,
    SubcategoryCategoryListView,
    ProductSubcategoryListView,
    ProductDetailView,
    AddReview
)


urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('categories/<slug:slug>/', SubcategoryCategoryListView.as_view(), name='categories'),
    path('subcategories/<slug:slug>/', ProductSubcategoryListView.as_view(), name='subcategories'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='products'),
    # path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path("reviews/", AddReview.as_view(), name="add_review"),
]