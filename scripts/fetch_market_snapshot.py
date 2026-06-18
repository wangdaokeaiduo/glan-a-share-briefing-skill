import urllib.request
import json
import sys

def fetch_json(url):
    import time
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urllib.request.urlopen(req, timeout=5) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            time.sleep(1)
    return None

def fetch_market_breadth():
    url = "http://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&secids=1.000001,0.399001&fields=f104,f105,f106"
    data = fetch_json(url)
    if data and data.get("data") and data["data"].get("diff"):
        sh = data["data"]["diff"][0]
        sz = data["data"]["diff"][1]
        total_up = sh.get('f104', 0) + sz.get('f104', 0)
        total_down = sh.get('f105', 0) + sz.get('f105', 0)
        total_flat = sh.get('f106', 0) + sz.get('f106', 0)
        
        print("### 📊 盘面涨跌幅情况 (Market Breadth)\n")
        print(f"- **上涨家数**: 🔴 {total_up} 家")
        print(f"- **下跌家数**: 🟢 {total_down} 家")
        print(f"- **平盘家数**: ⚪ {total_flat} 家")
        print()
    else:
        print("Error fetching market breadth\n")

def fetch_top_sectors():
    url = "http://push2bak.eastmoney.com/api/qt/clist/get?pn=1&pz=10&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:90+t:3+f:!50&fields=f14,f3,f128,f136"
    data = fetch_json(url)
    if data and data.get("data") and data["data"].get("diff"):
        print("### 🔥 实时板块热点 (Top 10 Sectors)\n")
        print("| 排名 | 板块名称 | 涨跌幅 | 领涨龙一 | 龙一涨幅 |")
        print("| --- | --- | --- | --- | --- |")
        for i, item in enumerate(data["data"]["diff"], 1):
            name = item.get('f14', '-')
            pct = item.get('f3', '-')
            leader = item.get('f128', '-')
            leader_pct = item.get('f136', '-')
            print(f"| {i} | {name} | {pct}% | {leader} | {leader_pct}% |")
        print()
    else:
        print("Error fetching top sectors\n")

def fetch_data(codes):
    if not codes:
        print("Error: No codes provided.")
        return

    formatted_codes = []
    for code in codes:
        code = code.lower().strip()
        if code.isdigit() and len(code) == 6:
            if code.startswith('6'):
                formatted_codes.append(f'sh{code}')
            else:
                formatted_codes.append(f'sz{code}')
        else:
            formatted_codes.append(code)

    url = f"http://qt.gtimg.cn/q={','.join(formatted_codes)}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = response.read().decode('gbk')
            
        print("### 📈 实时核心快照 (Core Quotes)\n")
        print("| 代码 | 名称 | 最新价 | 涨跌幅 | 昨收 | 今开 | 最高 | 最低 |")
        print("| --- | --- | --- | --- | --- | --- | --- | --- |")
        
        for line in data.split('\n'):
            line = line.strip()
            if not line:
                continue
            
            try:
                parts = line.split('"')[1].split('~')
                if len(parts) < 35:
                    continue
                name = parts[1]
                code = parts[2]
                price = parts[3]
                yest_close = parts[4]
                open_price = parts[5]
                pct_change = parts[32]
                high = parts[33]
                low = parts[34]
                
                print(f"| {code} | {name} | {price} | {pct_change}% | {yest_close} | {open_price} | {high} | {low} |")
            except Exception as e:
                pass
                
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_market_breadth()
    fetch_top_sectors()
    
    if len(sys.argv) > 1:
        if ',' in sys.argv[1]:
            codes = sys.argv[1].split(',')
        else:
            codes = sys.argv[1:]
        fetch_data(codes)
    else:
        # Default core indices and stocks
        default_codes = ["sh000001", "sz399001", "sz399006", "sh000688", "sz300308", "sh601138", "sh688008", "sh601398", "sh601088"]
        fetch_data(default_codes)

