# def two_sum(list,b):
#     sum = 0
#     for n in list:
#         if n+n==b:
#          sum = n+n
#     return sum
#         # else:
#         #    " wrong"

# list = [1,2,3,4,5,6]
# result = two_sum(list,3)
# print('result: ', result)def two_sum(list,b):
#     sum = 0
#     for n in list:
#         if n+n==b:
#          sum = n+n
#     return sum
#         # else:
#         #    " wrong"

# list = [1,2,3,4,5,6]
# result = two_sum(list,3)
# print('result: ', result)



# def twoSum(nums,target):
#   num_to_index = {}
#   for index, num in enumerate(nums):
#     complement = target - num
#     if complement in num_to_index:
#       return[num_to_index[complement], index]  # = [2,3]
#     num_to_index[num] = index
   
#   return -1




# nums=[19,23,30,4,15,61,17,28,90,10]
# target=21

# twoSumResult = twoSum(nums,target)
# print('twoSumResult: ', twoSumResult)

# a = 1044
# b = 733
# deff = a-b
# print('deff: ', deff)



  


































































































# def twoSum(nums,target):
#     gap = 1
#     for index, num in enumerate(nums):
#         n1 = num
#         while gap < len(nums):
#            n2 = nums[gap]
#            if n1 + n2 == target:
#               return [gap,index]
#            else:
#                return -1
              
          
              
  
# nums =[1,2,3,4,5,6,7,8,9,10]
# target=7
# twoSumResult = twoSum(nums,target)
# print('twoSumResult: ', twoSumResult)


     
# def find_palindrom(num):
#   reverse = ""
#   i = len(num) - 1
#   while i>=0:
#     reverse = reverse+num[i]
#     i-=1
#   if num==reverse:
#    return True
#   else:
#    return False





# x = "karak"
# result = find_palindrom(x)
# print('result: ', result)



# def twoSum(nums,target):
#  previndex = 0
#  currentindex = 1
#  step = 1
#  while currentindex<len(nums):
#    preValue = nums[previndex]
#    currentValue = nums[currentindex]
#    if preValue + currentValue == target:
#      return [previndex,currentindex]
#    elif preValue+currentValue!=target:
#        previndex = 0
#        step+=1
#        currentindex = step
#    else :
#        previndex=currentindex
#        currentindex+=1
#  return -1
     
# x = [1,2,3,4,5,6,7,8,9,10]
# y = 6
# result = twoSum(x,y)
# print('result: ', result)





















# def TwoSum(nums,target):
#   for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#       if nums[i]+nums[j]==target:
#         return [i,j]
#   return -1

# nums = [1,2,3,4,5,6,7,8,9,10]
# target = 7
# result = TwoSum(nums,target)
# print('result: ', result) 



# def common_latter(str):
  # for s in str:









strings = ['apple','apricot','peach']
list_of_sets=[]

for string in strings:
    list_of_sets.append(set(string))
    

answer = set()

for _set in list_of_sets:
    answer=answer.intersection(_set)



print('list_of_sets: ', answer)




