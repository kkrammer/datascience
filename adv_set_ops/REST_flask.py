# name = "Bob"
# greeting = "Hello, {}"
# with_name = greeting.format(name)

# print(with_name)

# size_input = input("How big is your house (in square feet): ")
# square_feet = int(size_input)
# square_meters = square_feet/10.8
# #print(square_meters)
# print(f"{square_feet} sq ft is {square_meters:.2f} sq meters")

friends = {"Bob","Rolf","Anne"}
abroad = {"Bob","Anne"}

#local_friends = friends.difference(abroad)
local_friends = abroad.difference(friends)
print(local_friends)