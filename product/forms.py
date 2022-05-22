from django import forms
from .models import Rating, Ratingstar, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }

class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=Ratingstar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)