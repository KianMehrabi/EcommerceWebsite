from store.models import Product

"""
    counts all the products
"""


def run():
    models = Product.objects.count()
    print("this database has ", models, " product(s)")
