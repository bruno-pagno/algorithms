# Complexity O(n * log n)
def merge_sort(arr):    
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    
    return arr
         

if __name__ == '__main__':
    print('Testing merge sort...')
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5,2,4,6,1,3]) == [1,2,3,4,5,6]
    assert merge_sort([6,5,4,3,2,1]) == [1,2,3,4,5,6]
    print('All tests passed')