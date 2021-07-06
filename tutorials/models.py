from django.db import models
from utils.validators.numbers import (
    validate_integer,
    validate_non_negative,
    validate_even,
    validate_odd
)


class Number(models.Model):
    """Test Number class for validators.
    
    NOTE: Validators will only run when used with ModelForm.
    Not by just calling save.
    """

    number = models.IntegerField(
        validators=[
            validate_integer, 
            validate_non_negative
        ]
    )
    odd = models.IntegerField(
        validators=[
            validate_integer, 
            validate_non_negative, 
            validate_odd
        ]
    )

    even = models.IntegerField(
        validators=[
            validate_integer, 
            validate_non_negative, 
            validate_even
        ]
    )

    characteristics = models.JSONField(default=dict)

    def __repr__(self) -> str:
        return "Number(number={}, odd={}, even={})".format(
            self.number,
            self.odd,
            self.even
        )