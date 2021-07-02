from django.forms import ModelForm

from tutorials.models import Number


class NumberForm(ModelForm):
    """Modelform for Number model."""

    class Meta:
        model = Number
        fields = [
            "number",
            "odd",
            "even"
        ]