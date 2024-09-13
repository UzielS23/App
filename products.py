import random

def get_random_products():
    products = [
        {'name': 'Laptop', 'price': '$799'},
        {'name': 'Smartphone', 'price': '$699'},
        {'name': 'Tablet', 'price': '$499'},
        {'name': 'Smartwatch', 'price': '$199'},
        {'name': 'Monitor', 'price': '$299'},
        {'name': 'Headphones', 'price': '$99'},
    ]
    return random.sample(products, 5)
