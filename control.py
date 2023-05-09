#1. Write a Python program that takes a list of strings as input and outputs the number of 
#times each string appears in the list, using a dictionary and conditional statements
names=["Faith","Ann","John","Joy","Ann"]
def people_names(names):
    name_count={}
    for name in names:
        if name not in name_count:
            name_count[name]=1
        else:
            name_count[name] +=1
    return name_count        

print(people_names(names))



#2.Write a Python program that takes a list of numbers as input and outputs the median of
# the numbers 
nums=[2,3,1,5,3,7]
def median(nums):
    nums.sort()
    x=len(nums)
    y=x/2
    







#3. Write a Python program that takes a list of numbers as input and outputs the second 
#largest number in the list using conditional statements and a for loop.
nums=[2,4,5,6,7,8]
def second_largest_number(nums):
    for num in nums:
        if num in num.max(nums)-2:
             print(num)   
        

            

        

        



#4.Write a Python program that takes a year as input and determines if it is a leap year
year=2012
if(year %4==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")    


#5.Write a Python program that takes a string as input and checks if it is a palindrome 
#(reads the same forwards and backwards), ignoring spaces and punctuation.
name="apple"
name1=reversed(name)
if name==name1:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")    