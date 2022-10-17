#take vowels as input,check whether its vowels or not
num = str(input("Enter a vowel:"))
v = "aeiouAEIOU"

if num in v:
    print("yes")
else:
    print("no")