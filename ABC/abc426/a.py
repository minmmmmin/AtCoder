X, Y = input().split()

order = ["Ocelot", "Serval", "Lynx"]

if order.index(X) >= order.index(Y):
    print("Yes")
else:
    print("No")
