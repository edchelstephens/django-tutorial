# [Models and Databases](https://docs.djangoproject.com/en/3.2/topics/db/)  

## Concrete(non abstract) model  
The single, definitive source of data about your data.  
Contains essential fields and behaviours of the data your storing.
Generally **each** concrete(not abstract) django **model,** **maps** to a single **database table**.

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.


# Fields
The most important part of a model – and the only required part of a model – is the list of database fields it defines. Fields are specified by class attributes. Be careful not to choose field names that conflict with the models API like **clean**, **save**, or **delete**.

# class Field
Field is an abstract class that represents a database table column. Django uses fields to create the database table (db_type()), to map Python types to database(get_prep_value()) and vice-versa(from_db_value()).

In models, a field is instantiated as a class attribute and represents a particular table column. 
It has attributes such as null and unique, and methods that Django uses to map the field value to database-specific values.

There are three main situations where Django needs to interact with the database backend and fields:

- when it queries the database (Python value -> database backend value)
- when it loads data from the database (database backend value -> Python value)
- when it saves to the database (Python value -> database backend value)


# Relationships  
Generally, ManyToManyField instances should go in the object that’s going to be edited on a form.  
In the example of Topping and Pizza, toppings is in Pizza (rather than Topping having a pizzas ManyToManyField ) because it’s more natural to think about a pizza having toppings than a topping being on multiple pizzas. 
The way it’s set up above, the Pizza form would let users select the toppings.  