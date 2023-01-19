from typing import List

# time complexity: O(n^2)
def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('Testing insertion sort...')
    assert insertion_sort([6,5,4,3,2,1]) == [1,2,3,4,5,6]
    assert insertion_sort([5,2,4,6,1,3]) == [1,2,3,4,5,6]
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    print('All tests passed')
