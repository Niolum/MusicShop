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
    CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    star = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Rating
        fields = ("star",)