#!/usr/bin/env python

username = {
    "admin"       : True ,
    "active"      : True ,
    "first_name"  : "Tatiana"   
}

if (username ["admin"]) == True:
    print(username["first_name"], "Admin") 
    if (username ["active"]) == True:
        print(username["first_name"], "Active")
        if bool(username["admin"] and ["active"]) == True:
            print("Active-Admin", str (username ["first_name"]))
else:
    print(username["username"])
    
