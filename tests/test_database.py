"""Тесты для класса Database"""
import pytest
from unittest.mock import patch, Mock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.test_data import TEST_BUNS, TEST_INGREDIENTS


class TestDatabase:
    """Тестовый класс для проверки класса Database"""
    
    def test_database_initialization(self):
        """Тест инициализации базы данных"""
        # Шаги теста
        database = Database()
        
        # Проверки
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
        
        # Проверяем типы объектов
        assert all(isinstance(bun, Bun) for bun in database.buns)
        assert all(isinstance(ing, Ingredient) for ing in database.ingredients)
    
    def test_available_buns_returns_list(self):
        """Тест метода available_buns"""
        # Шаги теста
        database = Database()
        buns = database.available_buns()
        
        # Проверки
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
    
    def test_available_ingredients_returns_list(self):
        """Тест метода available_ingredients"""
        # Шаги теста
        database = Database()
        ingredients = database.available_ingredients()
        
        # Проверки
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)
    
    def test_buns_have_correct_names_and_prices(self):
        """Тест правильности имен и цен булочек"""
        # Шаги теста
        database = Database()
        
        # Ожидаемые булочки из тестовых данных
        expected_buns = [
            TEST_BUNS[0],  # black bun, 100
            TEST_BUNS[1],  # white bun, 200
            TEST_BUNS[2],  # red bun, 300
        ]
        
        # Проверки
        for i, expected_bun in enumerate(expected_buns):
            assert database.buns[i].get_name() == expected_bun["name"]
            assert database.buns[i].get_price() == expected_bun["price"]
    
    def test_ingredients_have_correct_types_names_prices(self):
        """Тест правильности типов, имен и цен ингредиентов"""
        # Шаги теста
        database = Database()
        
        # Ожидаемые ингредиенты из тестовых данных
        expected_ingredients = [
            TEST_INGREDIENTS[0],  # SAUCE, hot sauce, 100
            TEST_INGREDIENTS[1],  # SAUCE, sour cream, 200
            TEST_INGREDIENTS[2],  # SAUCE, chili sauce, 300
            TEST_INGREDIENTS[4],  # FILLING, cutlet, 100
            TEST_INGREDIENTS[5],  # FILLING, dinosaur, 200
            TEST_INGREDIENTS[6],  # FILLING, sausage, 300
        ]
        
        # Проверки
        for i, expected_ingredient in enumerate(expected_ingredients):
            assert database.ingredients[i].get_type() == expected_ingredient["type"]
            assert database.ingredients[i].get_name() == expected_ingredient["name"]
            assert database.ingredients[i].get_price() == expected_ingredient["price"]
