def binarySearch(list, target):
   first = 0
   last = len(list) - 1
   done = False
   while first <= last and not done:
       mid = (first+last)//2
       if list[mid] == target:
           done = True
       else:
           if list[mid] > target:
               last = mid - 1
           else:
               first = mid + 1
   return done
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(test_list, 3))
print(binarySearch(test_list, 13))