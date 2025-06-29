
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

def test_merge_sort():
    test_cases = [
        [38, 27, 43, 3, 9, 82, 10],
        [1, 0, 45, -2, 99],
        [7, 2]
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        merge_sort(test_case)
        print(f"Sorted array {i}: {test_case}")

test_merge_sort()
