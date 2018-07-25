Lover1 =''
Lover2 =''
if(Lover1 == '' and Lover2 == ''):
     Lover1 = input("Please Enter Your Name: ").lower()
     Lover2 = input("Please Enter Your Loved Name: ").lower()
     concatenation = str(Lover1 + "love" + Lover2 )

     result={}
    
for letter in concatenation:
    if letter not in result.keys():
     	result[letter] = 1
    else:
    	result[letter] += 1

print(result)

