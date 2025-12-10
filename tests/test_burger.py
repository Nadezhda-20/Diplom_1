"""Тесты для класса Burger"""
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from tests.test_data import TEST_BUNS, TEST_INGREDIENTS


class TestBurger:
    """Тестовый класс для проверки класса Burger"""
    
    def test_init_creates_empty_burger(self):
        """Тест инициализации пустого бургера"""
        # Шаги теста
        burger = Burger()
        
        # Проверки
        assert burger.bun is None
        assert burger.ingredients == []
    
    def test_set_buns_sets_bun_correctly(self, mock_bun):
        """Тест установки булочки"""
        # Шаги теста
        burger = Burger()
        burger.set_buns(mock_bun)
        
        # Проверка
        assert burger.bun == mock_bun
    
    def test_add_ingredient_adds_to_list(self, mock_bun, mock_ingredient_sauce):
        """Тест добавления ингредиента"""
        # Шаги теста
        burger = Burger()



cat > tests/test_burger.py << EOF
"""Тесты для класса Burger"""
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from tests.test_data import TEST_BUNS, TEST_INGREDIENTS


class TestBurger:
    """Тестовый класс для проверки класса Burger"""
    
    def test_init_creates_empty_burger(self):
        """Тест инициализации пустого бургера"""
        # Шаги теста
        burger = Burger()
        
        # Проверки
        assert burger.bun is None
        assert burger.ingredients == []
    
    def test_set_buns_sets_bun_correctly(self, mock_bun):
        """Тест установки булочки"""
        # Шаги теста
        burger = Burger()
        burger.set_buns(mock_bun)
        
        # Проверка
        assert burger.bun == mock_bun
    
    def test_add_ingredient_adds_to_list(self, mock_bun, mock_ingredient_sauce):
        """Тест добавления ингредиента"""
        # Шаги теста
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        
        # Проверки
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce
