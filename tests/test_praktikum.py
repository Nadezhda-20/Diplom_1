import pytest
import sys
import os
import pytest
import runpy
from io import StringIO
from praktikum.praktikum import main


def test_main_executes():
    """Тест выполнения функции main"""
    main()


def test_main_has_output(capsys):
    """Тест, что main выводит результат"""
    main()
    captured = capsys.readouterr()
    assert captured.out != ""
    assert "Price:" in captured.out


def test_main_returns_none():
    """Тест, что main возвращает None"""
    result = main()
    assert result is None

def test_run_as_script():

    runpy.run_path('praktikum/praktikum.py', run_name='__main__')

def test_praktikum_as_main():
    """Тест для покрытия строки if __name__ == '__main__'"""
   
    original_stdout = sys.stdout
    
    try:
       
        sys.stdout = StringIO()        
        
        with open('praktikum/praktikum.py', 'r', encoding='utf-8') as f:
            code = f.read()
        
       
        namespace = {
            '__name__': '__main__',
            '__file__': 'praktikum/praktikum.py'
            
        }
        
        
        exec('from typing import List', namespace)
        exec('from praktikum.bun import Bun', namespace)
        exec('from praktikum.burger import Burger', namespace)
        exec('from praktikum.database import Database', namespace)
        exec('from praktikum.ingredient import Ingredient', namespace)
        
       
        exec(code, namespace)
        
        
        output = sys.stdout.getvalue()
        assert output != ""
        assert "Price:" in output
        
    finally:
        
        sys.stdout = original_stdout