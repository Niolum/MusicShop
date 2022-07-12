from django import forms
from .models import Rating, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }

class RatingForm(forms.ModelForm):
    CHOICES = [
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1)
    ]

    value = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Rating
        fields = ("value",)