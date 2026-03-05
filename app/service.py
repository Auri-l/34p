import random

PRODUCTS = {
    "tea": 120,
    "coffee": 180,
    "sandwich": 250
}

def calculate_total(product: str, qty: int) -> int:
    if qty < 0:
        raise ValueError("Количество не может быть отрицательным")
    if product not in PRODUCTS:
        raise ValueError("Неизвестный товар")

    price = PRODUCTS[product]
    return price * qty

def process_payment(amount: int) -> bool:
    if amount <= 0:
        return False  # логическая ошибка (не должна проходить)
    if random.random() < 0.2:
        raise RuntimeError("Payment gateway error")
    return True
