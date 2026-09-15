a = input("Enter your title: ")        # title (optional)
b = input("Your middle name: ")        # middle name (optional)
c = input("Last name: ")               # last name (optional)
d = input("Your Gender: ").strip().lower()

if d == "male":
    e = "MR. "
else:
    e = "MRS. "

name0 = a or e
name1 = b or "Zen"
name2 = c or "G"

print(name0, name1, name2)