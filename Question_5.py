def rotate(arr, n):
   arr = list(arr)  
   arr.insert(0, arr[n-1])
   arr.pop()
   print(arr)

n = 5
arr = {1, 2, 3, 4, 5}
rotate(arr, n)