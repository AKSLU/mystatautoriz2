import requests

def get_auth(login,password):
    url = "https://mapi.itstep.org/v1/mystat/auth/login"
    data = {"login":login,'password':password}
    r = requests.post(url,data = data)
    if r.status_code == 200:
        token = r.text
        try:
            
            return token
        except:
            print("Не ролучилось")
            return False
                    



def get_marks(token):
    url = "https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks"
    headers = {"authorization":f"Bearer {token}"}
    r = requests.get(url,headers=headers)
    if(r.status_code == 200):
        return r.json()
    else:
        return False
    
def get_schedule(token, type_):
    url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type={type_}"
    headers = {"authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            return r.json()
        except:
            print(f"Ошибка получения расписания ({type_}):")
            print(r.json())
            return []
    
  



            
        
        
    
