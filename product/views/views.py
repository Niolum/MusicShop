from django.shortcuts import get_object_or_404, render, redirect
from ..models import Category, Subcategory, Product, Brand, Rating
from ..service import ProductFilter, PaginationProducts
from django.views.generic import ListView, DetailView
from ..filters import SubcategoryFilter
from django.views.generic.base import View
from ..forms import RatingForm, ReviewForm
from django.http import HttpResponse



class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context
    # @staticmethod
    # def all_brands():
    #     return Brand.objects.all()
    # {{ view.all_brands }}


class SubcategoryCategoryListView(ListView):
    model = Subcategory
    slug_field = "url"
    allow_empty = False

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
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(subcategory__url=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProductSubcategoryListView, self).get_context_data(**kwargs)
        context['title'] = context['product_list'][0].subcategory
        return context


class ProductDetailView(DetailView):
    model = Product
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = context['product'].title
        product_id = context['product'].id
        # context['userrating'] = Rating.objects.filter(ip=get_client_ip(self.request), product_id=product_id)
        context["star_form"] = RatingForm()
        context["form"] = ReviewForm()
        return context


# class AddStarRating(View):

#     def post(self, request):
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             Rating.objects.update_or_create(
#                 ip=get_client_ip(self.request),
#                 product_id=int(request.POST.get("product")),
#                 defaults={'star_id': int(request.POST.get("star"))}
#             )
#             return HttpResponse(status=201)
#         else:
#             return HttpResponse(status=400)


class AddReview(View):

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())



