## 함수
def binarySearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary)-1

    while (start <= end) :
        mid = (start + end) // 2
        if ary[mid] == fData :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1

    return pos

# 전역변수
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162

# 메인
print('배열 -->', dataAry)
position = binarySearch(dataAry, findData)
if position == -1 :
    print(None)
else :
    print(position, 'position')