import requests as r
import sys

base_url = "https://www.v2e.fun"
checkin_url = base_url + "/user/checkin"


def main():
    if len(sys.argv) < 2:
        print("参数错误")
        exit(-1)
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
    except :
        print("登录态过期")
        exit(-1)
    
    if data['ret'] == 1:
        print("签到成功")
        exit(1)
    else:
        print("签到失败")
        exit(-1)
    

if __name__ == "__main__":
    main()