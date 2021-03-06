from django.urls import path
from product.views.views import (
    CategoryListView,
    SubcategoryCategoryListView,
    ProductSubcategoryListView,
    ProductDetailView,
    AddReview,
    AddStarRating,
    SearchResultView
)


urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('categories/<slug:slug>/', SubcategoryCategoryListView.as_view(), name='categories'),
    path('subcategories/<slug:slug>/', ProductSubcategoryListView.as_view(), name='subcategories'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='products'),
    path('add-rating/', AddStarRating.as_view(), name='add_rating'),
    path('reviews/<slug:slug>/', AddReview.as_view(), name="add_review"),
    path('search/', SearchResultView.as_view(), name='search_results')
]