"""Тесты для модуля praktikum.py"""
import pytest
from unittest.mock import Mock, patch
import sys
import io
from praktikum.praktikum import main


class TestPraktikum:
    """Тестовый класс для проверки модуля praktikum.py"""
    
    def test_main_function_executes_without_errors(self):
        """Тест, что функция main выполняется без ошибок"""
        # Шаги теста - просто вызываем функцию main
        # Она должна выполниться без исключений
        try:
            main()
            assert True  # Если дошли сюда, значит функция выполнилась без ошибок
        except Exception as e:
            pytest.fail(f"Функция main вызвала исключение: {e}")
    
    def test_main_prints_output(self, capsys):
        """Тест, что функция main выводит результат в консоль"""
        # Шаги теста
        main()
        
        # Перехватываем вывод
        captured = capsys.readouterr()
        
        # Проверки
        assert captured.out != ""  # Вывод не должен быть пустым
        assert "Price:" in captured.out  # В выводе должна быть цена
        assert "(====" in captured.out  # В выводе должны быть булочки
    
    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    def test_main_with_mocks(self, mock_burger_class, mock_database_class):
        """Тест функции main с моками для изоляции"""
        # Шаги теста
        # Создаем моки
        mock_database = Mock()
        mock_burger = Mock()
        
        # Настраиваем моки
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger
        
        # Настраиваем возвращаемые значения
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 100.0
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "Ingredient 1"
        mock_ingredient1.get_type.return_value = "SAUCE"
        mock_ingredient1.get_price.return_value = 50.0
        
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "Ingredient 2"
        mock_ingredient2.get_type.return_value = "FILLING"
        mock_ingredient2.get_price.return_value = 75.0
        
        # Настраиваем возвращаемые списки
        mock_database.available_buns.return_value = [mock_bun]
        mock_database.available_ingredients.return_value = [
            Mock(),  # ingredients[0]
            mock_ingredient1,  # ingredients[1] - используется в коде
            Mock(),  # ingredients[2]
            Mock(),  # ingredients[3] - используется в коде
            Mock(),  # ingredients[4] - используется в коде
            mock_ingredient2,  # ingredients[5] - используется в коде
        ]
        
        # Настраиваем возвращаемые значения для методов бургера
        mock_burger.get_price.return_value = 325.0
        mock_burger.get_receipt.return_value = "Test Receipt"
        
        # Вызываем функцию main
        main()
        
        # Проверяем, что методы были вызваны
        mock_database_class.assert_called_once()
        mock_burger_class.assert_called_once()
        mock_database.available_buns.assert_called_once()
        mock_database.available_ingredients.assert_called_once()
        
        # Проверяем, что методы бургера были вызваны с правильными параметрами
        mock_burger.set_buns.assert_called_once_with(mock_bun)
        assert mock_burger.add_ingredient.call_count == 4
        
        mock_burger.move_ingredient.assert_called_once_with(2, 1)
        mock_burger.remove_ingredient.assert_called_once_with(3)
        mock_burger.get_receipt.assert_called_once()
    
    def test_main_module_can_be_imported(self):
        """Тест, что модуль praktikum может быть импортирован"""
        # Шаги теста
        import praktikum.praktikum
        
        # Проверка
        assert hasattr(praktikum.praktikum, 'main')
        assert callable(praktikum.praktikum.main)
    
    def test_main_condition_block(self, monkeypatch, capsys):
        """Тест блока if __name__ == '__main__'"""
        # Сохраняем оригинальный stdout
        import sys
        original_stdout = sys.stdout
        
        try:
            # Захватываем вывод
            from io import StringIO
            captured_output = StringIO()
            sys.stdout = captured_output
            
            # Запускаем модуль как скрипт
            exec(open('praktikum/praktikum.py').read())
            
            # Получаем вывод
            output = captured_output.getvalue()
            
            # Проверяем, что вывод не пустой
            assert output != ""
            assert "Price:" in output
        finally:
            # Восстанавливаем stdout
            sys.stdout = original_stdout
