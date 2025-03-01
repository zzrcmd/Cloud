import requests
import json
from bs4 import BeautifulSoup
import os  # 新增：用于环境变量检查

print("=== 开始爬取数据 ===")

url = "https://hy1fly.github.io/YF-Cloud"  # 替换为实际目标地址
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    print(f"正在请求 URL: {url}")
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("请求成功，状态码:", response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    print("HTML 解析完成")

    data = {
        "title": soup.title.text.strip() if soup.title else "No Title",
        "content": soup.find('div', class_='content').text.strip() if soup.find('div', class_='content') else "No Content"
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("data.json 文件已生成")

except Exception as e:
    print(f"发生严重错误: {str(e)}")
    raise  # 抛出错误以便 Actions 捕获
