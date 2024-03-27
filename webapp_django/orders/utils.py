import random
def generate_product_name():
    # Sample list of product names (you can replace this with a larger dataset)
    product_names = [
        "Widget", "Gadget", "Tool", "Accessory", "Appliance", "Device", "Equipment",
        "Utensil", "Implement", "Contraption", "Instrument", "Apparatus", "Fixture",
        "Furniture", "Merchandise", "Article", "Commodity", "Merchandise", "Asset"
    ]
    a = random.choice(product_names)
    b = random.choice(product_names)
    if b == a:
        return f"{a}"
    return f"{a} {b}"
