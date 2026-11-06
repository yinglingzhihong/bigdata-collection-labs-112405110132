import requests

def get_img_data(url, headers):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        return res.content
    except Exception as e:
        print("请求异常：", e)
        return None

def save_img(save_path, img_bytes):
    if img_bytes:
        with open(save_path, "wb") as f:
            f.write(img_bytes)
            print(f"已保存：{save_path}")

if __name__ == "__main__":
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    img_url_list = [
        "http://www.bspider.top/static/yh31/images/202103302056530751.gif",
        "http://www.bspider.top/static/yh31/images/202103182029425871.jpg"
    ]
    save_dir = "./"
    for url in img_url_list:
        img_content = get_img_data(url, headers)
        filename = url.split("/")[-1]
        full_path = save_dir + filename
        save_img(full_path, img_content)
