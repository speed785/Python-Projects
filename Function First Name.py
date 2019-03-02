def firstName(fullname):
    firstSpace = fullname.index(" ")
    givenName = fullname[:firstSpace]
    return givenName

## Extract the first name from a full name.
fullName = input("Enter a person's full name: ")
print("First name:", firstName(fullName))
