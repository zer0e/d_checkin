import requests as r
import sys,time,datetime,base64

base64_base_url = "aHR0cHM6Ly9kb3VuYWkucHJv"
base_url = base64.b64decode(base64_base_url).decode()
index_url = base_url + "/user/pannel"
checkin_url = base_url + "/user/checkin"


def main():
    code = -1
    if len(sys.argv) < 2:
        print("参数错误")
        exit(code)
    cookie = sys.argv[1]
    last_15_days = datetime.date.today() + datetime.timedelta(days=15)
    last_15_days_time = int(time.mktime(time.strptime(str(last_15_days), '%Y-%m-%d')))
    cookie += ("expire_in=" + str(last_15_days_time))
    # exit()
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'referer': base_url + "/user/panel",
        'origin':'base_url',
        'x-requested-with': 'XMLHttpRequest',
        'cookie':cookie
    }
    h = r.get(index_url,headers=headers)
    h = r.post(checkin_url,headers= headers)
    try:
        data = h.json()
        print(data)
        if data['ret'] == 1:
            print("签到成功")
            code = 0 
        else:
            print("签到失败")
    except :
        print(f"登录态过期: {h.text}")
    
    exit(code)
    

if __name__ == "__main__":
    main()
