A,B = input().split()

if A == "sick" and B == "fine":
    print("2")

if A == "fine" and B == "fine":
    print("4")
    
if A == "sick" and B == "sick":
    print("1")
    
if A == "fine" and B == "sick":
    print("3")