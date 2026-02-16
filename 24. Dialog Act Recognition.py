text = input("Enter sentence: ")

if text.endswith("?"):
    print("Dialog Act: Question")
elif text.lower().startswith("please"):
    print("Dialog Act: Request")
else:
    print("Dialog Act: Statement")
