"""Фикстуры для тестов"""
import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient_sauce():
    """Фикстура для создания мока соуса"""
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "Test Sauce"
    ingredient.get_price.return_value = 50.0
    return ingredient


@pytest.fixture
def mock_ingredient_filling():
    """Фикстура для создания мока начинки"""
    ingredient = Mock()
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_name.return_value = "Test Filling"
    ingredient.get_price.return_value = 80.0
    return ingredient


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    """Фикстура для создания бургера с булочкой и ингредиентами"""
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger


@pytest.fixture
def mock_ingredient_1():
    """Фикстура для создания первого тестового ингредиента"""
    ingredient = Mock()
    ingredient.get_name.return_value = "Ingredient 1"
    ingredient.get_price.return_value = 10.0
    return ingredient


@pytest.fixture
def mock_ingredient_2():
    """Фикстура для создания второго тестового ингредиента"""
    ingredient = Mock()
    ingredient.get_name.return_value = "Ingredient 2"
    ingredient.get_price.return_value = 20.0
    return ingredient
