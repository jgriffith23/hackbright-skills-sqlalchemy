"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

Brand.query.get(8)
"""Example use of this query:

>>> brand_8 = Brand.query.get(8)
>>> brand_8
<Brand name=Austin, founded=1905, headquarters=Longbridge, England, discontinued=1987>
"""

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

"""Example usage of this query:

>>> corvettes = Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()
2016-08-07 00:08:20,348 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.name = %(name_1)s AND models.brand_name = %(brand_name_1)s
2016-08-07 00:08:20,350 INFO sqlalchemy.engine.base.Engine {'brand_name_1': 'Chevrolet', 'name_1': 'Corvette'}
>>> for corvette in corvettes:
...     print "%s, %s, %s" % (corvette.year, corvette.brand_name, corvette.name)
...
1953, Chevrolet, Corvette
1954, Chevrolet, Corvette
1955, Chevrolet, Corvette
1956, Chevrolet, Corvette
1957, Chevrolet, Corvette
1958, Chevrolet, Corvette
1959, Chevrolet, Corvette
1960, Chevrolet, Corvette
1961, Chevrolet, Corvette
1962, Chevrolet, Corvette
1963, Chevrolet, Corvette
1964, Chevrolet, Corvette
"""

# Get all models that are older than 1960.
db.session.query(Model).filter(Model.year < 1960).all()

"""Example usage of this query:

>>> old_cars = db.session.query(Model).filter(Model.year < 1960).all()
2016-08-07 00:04:14,065 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.year < %(year_1)s
2016-08-07 00:04:14,065 INFO sqlalchemy.engine.base.Engine {'year_1': 1960}
>>> for car in old_cars:
...     print "%s, %s, %s" % (car.year, car.brand_name, car.name)
...
1909, Ford, Model T
1926, Chrysler, Imperial
1950, Hillman, Minx Magnificent
1953, Chevrolet, Corvette
1954, Chevrolet, Corvette
1954, Cadillac, Fleetwood
1955, Chevrolet, Corvette
1955, Ford, Thunderbird
1956, Chevrolet, Corvette
1957, Chevrolet, Corvette
1957, BMW, 600
1958, Chevrolet, Corvette
1958, BMW, 600
1958, Ford, Thunderbird
1959, Austin, Mini
1959, Chevrolet, Corvette
1959, BMW, 600

"""

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

"""Example usage:

>>> relatively_recent_brands = Brand.query.filter(founded > 1920).all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'founded' is not defined
>>> relatively_recent_brands = Brand.query.filter(Brand.founded > 1920).all()
2016-08-07 00:03:02,488 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.founded > %(founded_1)s
2016-08-07 00:03:02,488 INFO sqlalchemy.engine.base.Engine {'founded_1': 1920}
>>> relatively_recent_brands
[<Brand name=Chrysler, founded=1925, headquarters=Auburn Hills, Michigan, discontinued=None, <Brand name=Fairthorpe, founded=1954, headquarters=Chalfont St Peter, Buckinghamshire, discontinued=1976, <Brand name=Pontiac, founded=1926, headquarters=Detroit, MI, discontinued=2010, <Brand name=Plymouth, founded=1928, headquarters=Auburn Hills, Michigan, discontinued=2001, <Brand name=Tesla, founded=2003, headquarters=Palo Alto, CA, discontinued=None]
"""

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

"""Example usage, showing the objects:

>>> cor_cars = Model.query.filter(Model.name.like('Cor%')).all()
2016-08-07 00:18:44,635 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.name LIKE %(name_1)s
2016-08-07 00:18:44,635 INFO sqlalchemy.engine.base.Engine {'name_1': 'Cor%'}
>>> cor_cars
[<Model year=1953 brand_name=Chevrolet name=Corvette>, <Model year=1954 brand_name=Chevrolet name=Corvette>, <Model year=1955 brand_name=Chevrolet name=Corvette>, <Model year=1956 brand_name=Chevrolet name=Corvette>, <Model year=1957 brand_name=Chevrolet name=Corvette>, <Model year=1958 brand_name=Chevrolet name=Corvette>, <Model year=1959 brand_name=Chevrolet name=Corvette>, <Model year=1960 brand_name=Chevrolet name=Corvair>, <Model year=1960 brand_name=Chevrolet name=Corvette>, <Model year=1961 brand_name=Chevrolet name=Corvette>, <Model year=1962 brand_name=Chevrolet name=Corvette>, <Model year=1963 brand_name=Chevrolet name=Corvair 500>, <Model year=1963 brand_name=Chevrolet name=Corvette>, <Model year=1964 brand_name=Chevrolet name=Corvette>]
"""

# Get all brands that were founded in 1903 and that are not yet discontinued.
db.session.query(Brand).filter(Brand.discontinued == None, Brand.founded == 1903).all()

""" Example usage:
>>> query = db.session.query(Brand).filter(Brand.discontinued == None, Brand.founded == 1903)
>>> query
<sqlalchemy.orm.query.Query object at 0x7f2c9a6780d0>
>>> operating_1903_brands = query.all()
2016-08-07 00:30:26,235 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.discontinued IS NULL AND brands.founded = %(founded_1)s
2016-08-07 00:30:26,235 INFO sqlalchemy.engine.base.Engine {'founded_1': 1903}
>>> operating_1903_brands
[<Brand name=Ford, founded=1903, headquarters=Dearborn, MI, discontinued=None, <Brand name=Buick, founded=1903, headquarters=Detroit, MI, discontinued=None]
"""

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
db.session.query(Brand).filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

"""Example usage:

>>> old_or_dead_brands = db.session.query(Brand).filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()
2016-08-07 00:35:59,392 INFO sqlalchemy.engine.base.Engine SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.discontinued IS NOT NULL OR brands.founded < %(founded_1)s
2016-08-07 00:35:59,392 INFO sqlalchemy.engine.base.Engine {'founded_1': 1950}
>>> old_or_dead_brands
[<Brand name=Ford, founded=1903, headquarters=Dearborn, MI, discontinued=None, <Brand name=Chrysler, founded=1925, headquarters=Auburn Hills, Michigan, discontinued=None, <Brand name=Citroen, founded=1919, headquarters=Saint-Ouen, France, discontinued=None, <Brand name=Hillman, founded=1907, headquarters=Ryton-on-Dunsmore, England, discontinued=1981, <Brand name=Chevrolet, founded=1911, headquarters=Detroit, Michigan, discontinued=None, <Brand name=Cadillac, founded=1902, headquarters=New York City, NY, discontinued=None, <Brand name=BMW, founded=1916, headquarters=Munich, Bavaria, Germany, discontinued=None, <Brand name=Austin, founded=1905, headquarters=Longbridge, England, discontinued=1987, <Brand name=Fairthorpe, founded=1954, headquarters=Chalfont St Peter, Buckinghamshire, discontinued=1976, <Brand name=Studebaker, founded=1852, headquarters=South Bend, Indiana, discontinued=1967, <Brand name=Pontiac, founded=1926, headquarters=Detroit, MI, discontinued=2010, <Brand name=Buick, founded=1903, headquarters=Detroit, MI, discontinued=None, <Brand name=Rambler, founded=1901, headquarters=Kenosha, Washington, discontinued=1969, <Brand name=Plymouth, founded=1928, headquarters=Auburn Hills, Michigan, discontinued=2001]
"""

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()

"""Example usage:

>>> non_chevys = Model.query.filter(Model.brand_name != "Chevrolet").all()
2016-08-07 00:40:23,117 INFO sqlalchemy.engine.base.Engine SELECT models.id AS models_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.brand_name != %(brand_name_1)s
2016-08-07 00:40:23,117 INFO sqlalchemy.engine.base.Engine {'brand_name_1': 'Chevrolet'}
>>> for model in non_chevys:
...     print model.year, model.brand_name, model.name
...
1909 Ford Model T
1926 Chrysler Imperial
1950 Hillman Minx Magnificent
1954 Cadillac Fleetwood
1955 Ford Thunderbird
1957 BMW 600
1958 BMW 600
1958 Ford Thunderbird
1959 Austin Mini
1959 BMW 600
1960 Fillmore Fillmore
1960 Fairthorpe Rockette
1961 Austin Mini Cooper
1961 Studebaker Avanti
1961 Pontiac Tempest
1962 Pontiac Grand Prix
1962 Studebaker Avanti
1962 Buick Special
1963 Austin Mini
1963 Austin Mini Cooper S
1963 Rambler Classic
1963 Ford E-Series
1963 Studebaker Avanti
1963 Pontiac Grand Prix
1964 Ford Mustang
1964 Ford Galaxie
1964 Pontiac GTO
1964 Pontiac LeMans
1964 Pontiac Bonneville
1964 Pontiac Grand Prix
1964 Plymouth Fury
1964 Studebaker Avanti
1964 Austin Mini Cooper
"""

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.

    Test:

    >>> get_model_info(1958)
    <BLANKLINE>
     Model: Thunderbird
     Brand name: Ford
     Brand HQ: Dearborn, MI
    ----------------
    <BLANKLINE>
     Model: Corvette
     Brand name: Chevrolet
     Brand HQ: Detroit, Michigan
    ----------------
    <BLANKLINE>
     Model: 600
     Brand name: BMW
     Brand HQ: Munich, Bavaria, Germany
    ----------------
    '''

    # Load models from the given year eagerly, so we don't have to query the database
    # every time we want to print the information.
    models_in_year = Model.query.options(db.joinedload("brand")).filter_by(year=year).all()

    # Print the name, brand, and HQ location for each model found
    for model in models_in_year:
        print "\n Model: %s\n Brand name: %s\n Brand HQ: %s\n----------------" % \
              (model.name, model.brand_name, model.brand.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
    using only ONE database query.

    Note: This docstest output is really too long to be here; it's drowning out
    the actual function. But creating a separate doctest file didn't make
    much sense in this context.

    >>> get_brands_summary()
    Ford Galaxie
    Ford Mustang
    Ford E-Series
    Ford Thunderbird
    Ford Thunderbird
    Ford Model T
    Chrysler Imperial
    Citroen ---
    Hillman Minx Magnificent
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvair 500
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvair
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvette
    Chevrolet Corvette
    Cadillac Fleetwood
    BMW 600
    BMW 600
    BMW 600
    Austin Mini Cooper
    Austin Mini Cooper S
    Austin Mini
    Austin Mini Cooper
    Austin Mini
    Fairthorpe Rockette
    Studebaker Avanti
    Studebaker Avanti
    Studebaker Avanti
    Studebaker Avanti
    Pontiac Grand Prix
    Pontiac Bonneville
    Pontiac LeMans
    Pontiac GTO
    Pontiac Grand Prix
    Pontiac Grand Prix
    Pontiac Tempest
    Buick Special
    Rambler Classic
    Plymouth Fury
    Tesla ---
    '''

    # Fetch a list of tuples containing the brand name and model name for all cars in the
    # database.
    brands_and_models = db.session.query(Brand.name, Model.name).outerjoin(Model).all()

    # I don't see a way to get all brands without doing another query using this method,
    # because there's a brand in the models table that has a model, but the brand is not
    # listed in the brands table. I'll write another function that gets objects instead.

    # Unpack tuples into two variables.
    for brand, model in brands_and_models:
        # Some brands don't have models. If the model exists, print brand and
        # model name. Otherwise, just print the brand and characters to indicate
        # a blank model.
        if model is None:
            print brand, "---"
        elif brand is None:
            print "---", model
        else:
            print brand, model


def get_brands_summary_objects():
    """Prints out each brand name, and each model name for that brand
    using only ONE database query. This time, uses a joinedload to get
    objects instead of tuples with just the data we need. """

    cars = Model.query.options(db.joinedload("brand")).all()

    # This for block is mostly the same as the one in the previous function. Now,
    # we just make an explicit check for if the brand actually isn't in the brands
    # table.

    # TODO: Ask someone who's managing the data in the database why Fillmore isn't
    # in the brands table...
    for car in cars:
        if car.name is None:
            print car.brand.name, "---"
        elif car.brand and car.brand_name is None:
            print "---", car.name
        elif car.brand is None:
            print car.brand_name, car.name
        else:
            print car.brand.name, car.name


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# The returned value is <flask_sqlalchemy.BaseQuery object at 0x7f439e447f10>, which is
# an object of the class flask_sqlalchemy.BaseQuery. This object represents the
# query itself, not any value(s) in the database.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#
# An association table is a table that only exists to relate two other tables to
# each other. Its fields don't actually tell you anything meaningful out of context
# because it only contains the primary keys of the two tables to connect.
#
# Association tables are used in true many-to-many relationships, unlike middle
# tables, which connect two one-to-many relationships to form a pseudo-many-to-many
# relationship.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(my_str):
    """Takes any string as a parameter. Returns a list of objects that are brands
    whose name contains or is equal to the input string."""

    # Get "lowercase", "Title Case", and "UPPERCASE" versions of the entered
    # string, to use in the like() methods for our search query. This works
    # given the nature of the data in the table.
    my_str_lower = my_str.lower()
    my_str_title = my_str.title()
    my_str_upper = my_str.upper()

    # Get all rows of brands table as objects. This technique works given the
    # nature of the data in the table.
    brands = Brand.query.filter((Brand.name.like("%" + my_str_lower + "%")) |
                                (Brand.name.like("%" + my_str_title + "%")) |
                                (Brand.name.like("%" + my_str_upper + "%"))).all()

    return brands



def get_models_between(start_year, end_year):
    pass
