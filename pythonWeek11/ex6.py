#recursive function to add 1 to num
def sumNumbers(num):
    if num:
        #num add num -1
        return num + sumNumbers(num - 1)
    else:
        
        return 0
#call function and get the result
result = sumNumbers(10)
#print result
print(result)