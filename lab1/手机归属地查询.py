import requests

def get_phone_html(url, headers, param):
    try:
        resp = requests.get(url, headers=headers, params=param, timeout=10)
        resp.raise_for_status()
        resp.encoding = "utf-8"
        return resp.text
    except Exception as err:
        print(err)
        return None

def save_html(filepath, html_text):
    if html_text:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_text)
        print("html页面保存完成")

if __name__ == "__main__":
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    url = "http://www.ip138.com/mobile.asp"
    params = {"mobile":"15052076791","action":"mobile"} # 把这里换成你的手机号
    html = get_phone_html(url, headers, params)
    save_html("phone_result.html", html)
