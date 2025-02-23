### 俩数组中位数问题
### 天际线问题
### 循环位移问题
转化为找最小元素位置
TODO 如何书写伪代码  
```python
def binarySearchForMin(X, low, high):
    if low == high:
        return low
    if high == low + 1:
        return low if X[low] < X[high] else high

    mid = (low + high) // 2

    if X[mid] <= X[high]:
        return binarySearchForMin(X, low, mid)
    else:
        return binarySearchForMin(X, mid + 1, high)
```