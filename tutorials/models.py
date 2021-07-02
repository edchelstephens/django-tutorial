from django.db import models
from utils.validators.numbers import (
    validate_integer,
    validate_non_negative,
    validate_even,
    validate_odd
)


class Number(models.Model):
    """Test Number class for validators."""

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

    def __repr__(self) -> str:
        return "Number(number={}, odd={}, even={})".format(
            self.number,
            self.odd,
            self.even
        )