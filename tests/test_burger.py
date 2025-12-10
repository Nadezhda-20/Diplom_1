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

    @pytest.mark.parametrize("index_to_remove, expected_count", [
        (0, 1),  # Удаление первого ингредиента
        (1, 1),  # Удаление второго ингредиента
    ])
    def test_remove_ingredient_removes_correctly(self, burger_with_ingredients, 
                                                  index_to_remove, expected_count):
        """Тест удаления ингредиента по индексу с параметризацией"""
        # Шаги теста
        initial_count = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(index_to_remove)
        
        # Проверка
        assert len(burger_with_ingredients.ingredients) == expected_count
    
    @pytest.mark.parametrize("from_index, to_index, expected_order", [
        (0, 1, [1, 0]),  # Первый элемент перемещается на место второго
        (1, 0, [1, 0]),  # Второй элемент перемещается на место первого
        (0, 0, [0, 1]),  # Элемент перемещается на ту же позицию
    ])
    def test_move_ingredient_moves_correctly(self, mock_bun,
                                             from_index, to_index, expected_order):
        """Тест перемещения ингредиента с параметризацией"""
        # Шаги теста
        burger = Burger()
        burger.set_buns(mock_bun)
        
        # Создаем два разных мока
        ingredient1 = Mock()

cat >> tests/test_burger.py << EOF

    @pytest.mark.parametrize("index_to_remove, expected_count", [
        (0, 1),  # Удаление первого ингредиента
        (1, 1),  # Удаление второго ингредиента
    ])
    def test_remove_ingredient_removes_correctly(self, burger_with_ingredients, 
                                                  index_to_remove, expected_count):
        """Тест удаления ингредиента по индексу с параметризацией"""
        # Шаги теста
        initial_count = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(index_to_remove)
        
        # Проверка
        assert len(burger_with_ingredients.ingredients) == expected_count
    
    @pytest.mark.parametrize("from_index, to_index, expected_order", [
        (0, 1, [1, 0]),  # Первый элемент перемещается на место второго
        (1, 0, [1, 0]),  # Второй элемент перемещается на место первого
        (0, 0, [0, 1]),  # Элемент перемещается на ту же позицию
    ])
    def test_move_ingredient_moves_correctly(self, mock_bun,
                                             from_index, to_index, expected_order):
        """Тест перемещения ингредиента с параметризацией"""
        # Шаги теста
        burger = Burger()
        burger.set_buns(mock_bun)
        
        # Создаем два разных мока
        ingredient1 = Mock()
        ingredient1.get_name.return_value = "Ingredient 1"
        
        ingredient2 = Mock()
        ingredient2.get_name.return_value = "Ingredient 2"
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        burger.move_ingredient(from_index, to_index)
        
        # Проверка
        if expected_order == [1, 0]:
            assert burger.ingredients[0] == ingredient2
            assert burger.ingredients[1] == ingredient1
        else:  # [0, 1]
            assert burger.ingredients[0] == ingredient1
            assert burger.ingredients[1] == ingredient2
    
    @pytest.mark.parametrize("bun_price, sauce_price, filling_price, expected_total", [
        (100.0, 50.0, 80.0, 100.0 * 2 + 50.0 + 80.0),  # Все цены положительные
        (0.0, 0.0, 0.0, 0.0),  # Все бесплатные
        (50.5, 25.25, 75.75, 50.5 * 2 + 25.25 + 75.75),  # Дробные цены
    ])
    def test_get_price_calculates_correctly(self, bun_price, sauce_price, 
                                            filling_price, expected_total):
        """Тест расчета цены бургера с параметризацией"""
        # Шаги теста
        burger = Burger()
        
        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        
        sauce_mock = Mock()
        sauce_mock.get_price.return_value = sauce_price
        
        filling_mock = Mock()
        filling_mock.get_price.return_value = filling_price
        
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        
        # Проверка
        assert burger.get_price() == expected_total
    
    def test_get_price_without_bun_raises_exception(self):
        """Тест расчета цены без установленной булочки"""
        # Шаги теста
        burger = Burger()
        
        # Проверка
        assert burger.bun is None
    
    def test_get_receipt_formats_correctly(self, burger_with_ingredients):
        """Тест формирования чека"""
        # Шаги теста
        burger_with_ingredients.bun.get_name.return_value = "Test Bun"
        
        sauce_mock = burger_with_ingredients.ingredients[0]
        sauce_mock.get_type.return_value = "SAUCE"
        sauce_mock.get_name.return_value = "Test Sauce"
        
        filling_mock = burger_with_ingredients.ingredients[1]
        filling_mock.get_type.return_value = "FILLING"
        filling_mock.get_name.return_value = "Test Filling"
        
        # Мокаем get_price для предсказуемой цены
        burger_with_ingredients.get_price = Mock(return_value=330.0)
        
        receipt = burger_with_ingredients.get_receipt()
        
        # Ожидаемый чек
        expected_receipt_lines = [
            "(==== Test Bun ====)",
            "= sauce Test Sauce =",
            "= filling Test Filling =",
            "(==== Test Bun ====)",
            "",
            "Price: 330.0"
        ]
        expected_receipt = "\n".join(expected_receipt_lines)
        
        # Проверка полного соответствия
        assert receipt == expected_receipt
    
    def test_get_receipt_with_single_ingredient(self, mock_bun, mock_ingredient_sauce):
        """Тест формирования чека с одним ингредиентом"""
        # Шаги теста
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        
        burger.bun.get_name.return_value = "Single Bun"
        mock_ingredient_sauce.get_type.return_value = "SAUCE"
        mock_ingredient_sauce.get_name.return_value = "Single Sauce"
        
        # Мокаем get_price
        burger.get_price = Mock(return_value=250.0)
        
        receipt = burger.get_receipt()
        
        # Ожидаемый чек
        expected_receipt_lines = [
            "(==== Single Bun ====)",
            "= sauce Single Sauce =",
            "(==== Single Bun ====)",
            "",
            "Price: 250.0"
        ]
        expected_receipt = "\n".join(expected_receipt_lines)
        
        # Проверка полного соответствия
        assert receipt == expected_receipt
    
    def test_get_receipt_with_no_ingredients(self, mock_bun):
        """Тест формирования чека без ингредиентов"""
        # Шаги теста
        burger = Burger()
        burger.set_buns(mock_bun)
        
        burger.bun.get_name.return_value = "Bun Only"
        burger.get_price = Mock(return_value=200.0)
        
        receipt = burger.get_receipt()
        
        # Ожидаемый чек
        expected_receipt_lines = [
            "(==== Bun Only ====)",
            "(==== Bun Only ====)",
            "",
            "Price: 200.0"
        ]
        expected_receipt = "\n".join(expected_receipt_lines)
        
        # Проверка полного соответствия
        assert receipt == expected_receipt
