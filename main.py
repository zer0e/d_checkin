import requests as r
import sys

base_url = "https://aaaa.gay"
checkin_url = base_url + "/user/checkin"


def main():
    code = -1
    if len(sys.argv) < 2:
        print("参数错误")
        exit(code)
    cookie = sys.argv[1]
    # print(cookie.split(";"))
    # exit()
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'referer': base_url + "/user/panel",
        'cookie':cookie
    }
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
        print("登录态过期")
    
    exit(code)
    

if __name__ == "__main__":
    main()
