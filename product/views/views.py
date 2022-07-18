from django.db import models
from django.shortcuts import get_object_or_404, redirect
from ..models import Category, ProductPhoto, Subcategory, Product, Brand, Rating
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from ..forms import RatingForm, ReviewForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin



class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context


class SubcategoryCategoryListView(ListView):
    model = Subcategory
    slug_field = "url"

    def get_queryset(self):
        return Subcategory.objects.filter(category__url=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(SubcategoryCategoryListView, self).get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['title'] = context['subcategory_list'][0].category
        return context


class ProductSubcategoryListView(ListView):
    model = Product
    slug_field = "url" 
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(subcategory__url=self.kwargs['slug']).select_related('subcategory')

    def get_context_data(self, **kwargs):
        context = super(ProductSubcategoryListView, self).get_context_data(**kwargs)
        context['title'] = context['product_list'][0].subcategory
        return context


class ProductDetailView(DetailView):
    model = Product
    slug_field = "url"

    def get_queryset(self):
        products = Product.objects.filter(draft=False).annotate(
            middle_star=models.Sum(models.F('ratings__value')) / models.Count(models.F('ratings'))
        )
        return products

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = context['product'].title
        context['reviews'] = context['product'].get_review().select_related('parent').select_related('user')
        product_id = context['product'].id
        context['photos'] = ProductPhoto.objects.filter(product_id=product_id).select_related('product')
        context["star_form"] = RatingForm()
        context["form"] = ReviewForm()
        context["middle_star"] = context['product'].middle_star
        return context


class AddStarRating(View):

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                user=request.user,
                product_id=int(request.POST.get("product")),
                defaults={'value': float(request.POST.get("value"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class AddReview(LoginRequiredMixin, View):
    login_url = '/users/accounts/login/'

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        product = get_object_or_404(Product, url=self.kwargs['slug'])
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.user = request.user
            form.save()
            return redirect(product.get_absolute_url())


class SearchResultView(ListView):
    model = Product
    paginate_by = 3
    template_name = 'product/product_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(Q(title__icontains=query) | Q(brand__title__icontains=query) | 
        Q(subcategory__title__icontains=query)).select_related('subcategory')
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        context['title'] = 'Результаты поиска'
        return context