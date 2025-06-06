from core import *

def test_auth():
    token = get_auth("Utemb_aa50","lookism20062007#A")
    return token!= False

def testt():
    token = get_auth("test","test")
    return token == False

print(test_auth())
print(testt)


    
