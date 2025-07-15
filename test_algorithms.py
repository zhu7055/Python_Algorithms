# 假設您有一個名為 'my_algorithms.py' 的檔案，其中有一個函數
# def add_numbers(a, b):
#     return a + b

# 您的測試檔案 test_algorithms.py
import sys
import os

# 假設您的演算法程式碼在 'your_project_name/' 下
# 為了讓測試能找到您的演算法模組，可能需要調整 PYTHONPATH 或相對路徑導入
# 一個常見的解決方案是確保 pytest 在專案根目錄運行
# 如果您的演算法程式碼在子目錄中，您可能需要這樣導入：
# from your_module_name.your_algorithm_file import your_function

# 簡單的測試函數範例
def test_addition():
    result = 2 + 3
    assert result == 5

def test_multiplication():
    result = 2 * 3
    assert result == 6

# 如果您有實際的演算法函數，例如在 algorithms/sort.py 中有一個 quick_sort 函數
# 並且您的 CI 運行目錄在專案根目錄
# from algorithms.sort import quick_sort # 假設有這個路徑
# def test_quick_sort():
#     arr = [3, 1, 4, 1, 5, 9, 2, 6]
#     quick_sort(arr)
#     assert arr == [1, 1, 2, 3, 4, 5, 6, 9]
