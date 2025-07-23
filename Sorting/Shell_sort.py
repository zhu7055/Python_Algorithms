# Shell Sort
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def ShellSort(data):
    n = len(data)  # 獲取data長度
    gap = n // 2  # 初始化間隔，設為數組長度的一半
    while gap > 0:  # 當間隔大於0時循環
        for i in range(gap, n):  # 從間隔位置開始遍歷數組
            temp = data[i]  # 暫存當前元素
            j = i  # 設置 j 為當前索引
            while j >= gap and data[j-gap] > temp:  # 如果 j 大於等於間隔且前一個間隔的元素大於暫存元素
                data[j] = data[j-gap]  # 將前一個間隔的元素移到當前位置
                j = j - gap  # 將 j 向前移動一個間隔
            data[j] = temp  # 將暫存元素放到正確位置
        gap = gap // 2  # 縮小間隔
    return data  # 返回排序後的數據

print(ShellSort(data))  # 印排序結果
# 輸出: [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]
