# How to read a specific element, value, in my case an IP, from a list

list = ["192.168.56.101", "192.34.45.230"]
m = "192.168.56.101"

if m in list:
    print(f"yes, {m}")
else:
    print("no")
