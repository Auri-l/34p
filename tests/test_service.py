import pytest
from app.service import calculate_total, process_payment

def test_calculate_total_ok():
    assert calculate_total("coffee", 2) == 360

def test_calculate_total_zero():
    assert calculate_total("tea", 0) == 0

def test_unknown_product():
    with pytest.raises(ValueError, match="Неизвестный товар"):
        calculate_total("unknown_product", 1)

def test_negative_quantity():
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        calculate_total("coffee", -1)

def test_process_payment_negative_amount():
    assert process_payment(-100) is False