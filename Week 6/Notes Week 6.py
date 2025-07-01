# Byte of python

def reverse(text):
    return text[::-1]

def is_palendrome(text):
    return text == reverse(text)

something = input("Enter text: ")
if is_palendrome(something):
    print("Yes, it is a palendrome")
else:
    print("No, it is not a palendrome")


