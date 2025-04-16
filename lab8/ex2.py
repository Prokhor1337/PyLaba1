list1 = input("Введи перший список чисел через пробіл: ").split()
list2 = input("Введи другий список чисел через пробіл: ").split()

try:
    nums1 = list(map(int, list1))
    nums2 = list(map(int, list2))
except ValueError:
    print("Списки мають містити лише числа.")
    nums1 = nums2 = []

merged = list(set(nums1 + nums2))
merged.sort()

print("Результат:", merged)
