from django import forms
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.



class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "image")
    list_display_links = ("title", )


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name", "email")


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_descripton = "Изображение"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "subcategory", "url", "draft")
    list_filter = ("subcategory", "brand")
    search_fields = ("title", "subcategory__title", "brand__title")
    inlines = [ProductPhotoInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    form = ProductAdminForm
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title", "brand", "subcategory"),)
        }),
        (None, {
            "fields": ("description", ("image", "get_image"),),
        }),
        (None, {
            "fields": (("price", "stock"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Изображение"


    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")


    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ("change",)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ("change",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "product")
    readonly_fields = ("name", "email")


@admin.register(Subcategory)
class SubcategoyAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_descripton = "Изображение"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=auto height="110"')

    get_image.short_descripton = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "product", "ip")


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "product", "get_image")
    readonly_fields = ("get_image",)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.register(Ratingstar)