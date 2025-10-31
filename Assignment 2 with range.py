name = {} #Empty dictionary created to store taken values
for _ in range(5): #runs the code 5 times
    s_name=input("Give Name: ")
    marks=int(input("Marks: "))
    if marks >= 90:
        give= "A"
    elif marks >= 75:
        give= "B"
    elif marks >= 50:
        give= "C"
    else:
        give= "F"
    name[s_name]=give # makes the s_name and give be inserted into the dictionary
for s_name, give in name.items():
    print(f"{s_name}:{give}")
