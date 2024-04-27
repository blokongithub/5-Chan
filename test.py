import hashlib
 
# initializing string
str2hash = "5ChanClone"
 
# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())

#hashcat -a 3 -m 0 e0d1e169daaa03df020a8aa6172becd0