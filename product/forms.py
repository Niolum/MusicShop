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
        (5, 5.0),
        (4, 4.0),
        (3, 3.0),
        (2, 2.0),
        (1, 1.0)
    ]

    value = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Rating
        fields = ("value",)