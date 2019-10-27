string = 'SUBSCRIBE real madrid'
if string.__contains__("SUBSCRIBE"):
    print("YES")

string = 'SUBSCRIB real madrid'
if string.__contains__("SUBSCRIBE"):
    print("YES")
else:
    print("NO")