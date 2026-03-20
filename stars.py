''' 
   *
  ***
 *****

'''


# a=int(input("Enter the number"))
# for i in range(1,a+1):
#     print(" "*(a-i+1)+"*"*(2*i-1))
    


a=int(input("Enter the number"))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1),end="")
    print("")

