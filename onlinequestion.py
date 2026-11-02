# nums = [1,5,0,3,5]
# def find_smallest():
    

#     smallest = float("inf")
#     smallest2 = float("inf")

#     for i in nums:
#         if i<smallest:
#             smallest2 = smallest 
#             smallest = i 
            
#         elif i<smallest2 and i>smallest:
            
#             smallest2 = i
    
#     print(smallest2) 
    
# find_smallest()

# TAREEKA THODA GALAT HAI ACHHE SE TRY KRO 


a = [1,2,2,4]
freq = {}
list = []
original_sum = 0
a_sum = 0

for i in a:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
     
     
for i in freq:
    if  freq[i] == 2:
        list.append(i)
        
for i in a:
    a_sum += i 
    
for i in range(1,len(a)):
    original_sum += i
    
ans = a_sum - original_sum
list.append(ans)

print(list)
        
        
    
    

    