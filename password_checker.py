# Password Checker by Ashley Meza

test = "James"
first_char = test[0]


print(first_char.isupper())

# islower()

print(test.find("a") )
# Return the Index if it finds it
# Retuns -1 if it can't find it

# Step 1:
# Prompt the user to enter their password
# Check the following:
# - If the password contains the letter z (Hint: use .find())
# - If the password end with an !
# - If the password begins with any uppercase letter
# If yes, to all thes, print "Accept!"
# If any of these are not true, print "Reject!"

# Step 2: Implement the more generic rules on the whiteboard
# - Hint: You may want to put the symbols into a list of symbols,
# which you can check against
str1 = """ 
Please enter a password with the follwing requirements which must include: 
 - At least 8 characters, no more than 15"
 - Includes a "!"
 - Contains the letter "z"
 - Begins with an uppercase letter
"""
password = "pw"
# pw_length = (15>=8)
print(str1)

pw = input("Enter password here: ")

if 8 <= len(pw) <= 15 :
    print("Accept!")
else:
    print("Decline! You must include 8-15 characters.") 
   
# (15>=8):
  
if "z" in pw:
    print("Accept!")
else:
    print("Decline!" + " You must include a 'z'.")

     
if pw[-1] == "!":
    print("Accept!")
else: 
    print("Decline! You must include a '!'")

# print(test.find("z"))
# print(test.find("!"))
# print(test.find("isupper"))


