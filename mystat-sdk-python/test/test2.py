from core import *

def test_auth():
    token = get_auth("Utemb_aa50","lookism20062007#A")
    return token!= False

def testt():
    token = get_auth("test","test")
    return token == False

def test_marks():
    token = get_auth("Utemb_aa50","lookism20062007#A")
    marks = get_marks(token)
    return isinstance(marks,list)
    return token!= False

def test_week_schedule():
    token = get_auth("Utemb_aa50","lookism20062007#A")
    week = get_schedule(token,"week")
    return isinstance(week,dict)
    return token!= False


def test_month_schedule():
    token = get_auth("Utemb_aa50","lookism20062007#A")
    month = get_schedule(token,"month")
    return isinstance(month,dict)
    return token!= False

print("авторизация ",test_auth())
print("False авторизация ",testt())
print("test_marks ",test_marks())
print("test_week_schedule ",test_week_schedule())
print("test_month_schedule ",test_month_schedule())




    
