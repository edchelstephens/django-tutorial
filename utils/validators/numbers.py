from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_integer(value):
    """Validate value is integer."""
    if not isinstance(value, int):
        raise ValidationError(
            _("%(value)s is not an integer"),
            params={"value": value}
        )

def validate_non_negative(value):
    """Validate non negative value."""
    validate_integer(value)
    if value < 0:
        raise ValidationError(
            _("%(value)s is negative"),
            params={"value": value}
        )

def validate_even(value):
    """Validate even value."""
    validate_integer(value)
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value}
        )

def validate_odd(value):
    """Validate odd value."""
    validate_integer(value)
    if value %2 != 1:
        raise ValidationError(
            _("%(value)s is not an odd number"),
            params={"value": value}
        )