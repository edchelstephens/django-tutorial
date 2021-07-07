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


class Blog(models.Model):

    name = models.CharField(max_length=50)

    def __repr__(self) -> str:
        return "Blog(name={})".format(self.name)


class Entry(models.Model):

    title = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name="blog_entries")


    def __repr__(self) -> str:
        return "Entry(title={}, blog={})".format(
            self.title,
            repr(self.blog)
        )



class Topping(models.Model):

    name = models.CharField(max_length=50)


    def __repr__(self) -> str:
        return "Topping(name={}, pizzas={})".format(
            self.name,
            self.get_pizzas(),
            
        )

    def __str__(self) -> str:
        return self.name

    def get_pizzas(self):
        return [ str(p) for p in self.pizza_set.all()]

class Pizza(models.Model):

    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __repr__(self) -> str:
        return "Pizza(name={}, toppings={})".format(
            self.name,
            self.get_toppings()
        )

    def __str__(self) -> str:
        return self.name


    def get_toppings(self):
        return [ t for t in self.toppings.all() ]