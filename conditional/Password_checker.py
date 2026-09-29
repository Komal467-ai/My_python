user=input("enter your passward")

if len(user) <=6:
    print("your passward i weak")

elif len(user)<=10:
    print("your password is medium")

else:
    print("your password is strong")