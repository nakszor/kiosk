from menu import products
from typing import List, Dict

def calculate_tab(table_consumption: List[Dict]) -> Dict:
    subtotal = 0
    for item in table_consumption:
        product_id = item["_id"]
        amount = item["amount"]
        for product in products:
            if product["_id"] == product_id:
                subtotal += product["price"] * amount
                break
    
    return {"subtotal": f"${subtotal:.2f}".rstrip('0').rstrip('.')}

