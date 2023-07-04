from menu import products
from typing import List, Dict

def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
    
    for product in products:
        if product["_id"] == id:
            return product
    
    return {}

def get_products_by_type(product_type: str):
    if not isinstance(product_type, str):
        raise TypeError("product type must be a str")
    
    result = []
    for product in products:
        if product["type"] == product_type:
            result.append(product)
    
    return result

def add_product(menu: List[Dict], **product: Dict) -> Dict:
    new_id = 1
    if len(menu) > 0:
        max_id = max([p['_id'] for p in menu])
        new_id = max_id + 1
    product['_id'] = new_id
    menu.append(product)
    return product

def menu_report():
    product_count = len(products)

    total_price = sum(product['price'] for product in products)
    average_price = round(total_price / product_count, 2)

    types_count = {}
    for product in products:
        product_type = product['type']
        types_count[product_type] = types_count.get(product_type, 0) + 1
    most_common_type = max(types_count, key=types_count.get)

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
