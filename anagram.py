str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# remove spaces
str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")
# change all letters to upper case
str1 = str1.upper()
str2 = str2.upper()
# convert string into list
str1 = list(str1)
str2 = list(str2)
# sort the list
str1.sort()
str2.sort()

str1 = "".join(str1)
str2 = "".join(str2)
# compare both strings
# Anagrams must have the same letters used the same amount of time
if str1 == str2:
    print("Anagrams")
else:
    print("Not anagrams")