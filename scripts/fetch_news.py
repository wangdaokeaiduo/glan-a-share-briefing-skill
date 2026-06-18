import json
import urllib.request
import re

def fetch_sina_7x24_news(limit=15):
    # Sina 7x24 News API (id 152 is Global/Financial News)
    url = f"https://zhibo.sina.com.cn/api/zhibo/feed?page=1&page_size={limit}&zhibo_id=152"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            print("### 📡 实时快讯 API 获取结果 (Real-time News API)\n")
            
            if data.get('result') and data['result'].get('data'):
                items = data['result']['data'].get('feed', {}).get('list', [])
                for item in items:
                    time_str = item.get('create_time', '')
                    text = item.get('rich_text', '').strip()
                    
                    # Clean up HTML tags if any
                    text = re.sub(r'<[^>]+>', '', text)
                    
                    if text:
                        print(f"- **[{time_str}]** {text}")
                print()
            else:
                print("No news found or API changed.\n")
    except Exception as e:
        print(f"Error fetching Sina news: {e}\n")

if __name__ == "__main__":
    fetch_sina_7x24_news(20)
