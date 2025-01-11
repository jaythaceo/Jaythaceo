
# Let's do some stuff here.
# Now maybe a class is needed?

def bubble_sort(arr):
  """" Sorts a list using bubblesort """
  n = len(arr)

  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j +1]:
        arr[j], arr[j +1] = arr[j +1], arr[j]


  return arr
 



my_list = [123,34,254,7866,53]
print("Unsorted list:", my_list)
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)