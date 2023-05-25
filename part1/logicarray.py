def move_elements(arr1, arr2):
    arr2.extend(arr1)
    return arr2

# Initial arrays
arr1 = [1, 2]
arr2 = [2, 3]
arr3 = [3, 4]
arr4 = [5, 6]

print("Initial arrays:")
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)

# Delete arr1 and move its values to the nearest arr2
if arr1 in [arr1, arr2, arr3, arr4]:
    index = [arr1, arr2, arr3, arr4].index(arr1)
    del [arr1, arr2, arr3, arr4][index]
    if index < len([arr1, arr2, arr3, arr4]):
        [arr1, arr2, arr3, arr4][index] = move_elements(arr1, [arr1, arr2, arr3, arr4][index])
    elif len([arr1, arr2, arr3, arr4]) > 0:
        [arr1, arr2, arr3, arr4][-1] = move_elements(arr1, [arr1, arr2, arr3, arr4][-1])
    arr1 = []

print("\nAfter deleting arr1 and moving its values to the nearest arr2:")
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)

# Delete arr2 and move its values to the nearest arr3
if arr2 in [arr1, arr2, arr3, arr4]:
    index = [arr1, arr2, arr3, arr4].index(arr2)
    del [arr1, arr2, arr3, arr4][index]
    if index < len([arr1, arr2, arr3, arr4]):
        [arr1, arr2, arr3, arr4][index] = move_elements(arr2, [arr1, arr2, arr3, arr4][index])
    elif len([arr1, arr2, arr3, arr4]) > 0:
        [arr1, arr2, arr3, arr4][-1] = move_elements(arr2, [arr1, arr2, arr3, arr4][-1])
    arr2 = []

print("\nAfter deleting arr2 and moving its values to the nearest arr3:")
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)

# Delete arr3 and move its values to the nearest arr4
if arr3 in [arr1, arr2, arr3, arr4]:
    index = [arr1, arr2, arr3, arr4].index(arr3)
    del [arr1, arr2, arr3, arr4][index]
    if index < len([arr1, arr2, arr3, arr4]):
        [arr1, arr2, arr3, arr4][index] = move_elements(arr3, [arr1, arr2, arr3, arr4][index])
    elif len([arr1, arr2, arr3, arr4]) > 0:
        [arr1, arr2, arr3, arr4][-1] = move_elements(arr3, [arr1, arr2, arr3,arr1][index])
    arr3 = []

print("\nAfter deleting arr3 and moving its values to the nearest arr4:")
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)
