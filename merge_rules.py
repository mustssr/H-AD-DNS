import requests

# 这是你要整合的规则源 URL 列表
urls = [
    "https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/refs/heads/main/assets/filter_53.txt",
    "https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/refs/heads/main/assets/filter_50.txt",
    "https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/refs/heads/main/assets/filter_8.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/tif.mini.txt",
    "https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/refs/heads/main/assets/filter_45.txt",
    "https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/refs/heads/main/assets/filter_48.txt"
]

# 用于存放所有规则的集合（set），集合可以自动去重
all_rules = set()

# 遍历 URL 列表
for url in urls:
    try:
        # 发起网络请求获取规则内容
        response = requests.get(url, timeout=60)
        # 如果请求成功
        if response.status_code == 200:
            # 按行分割文本，并去除每行首尾的空白字符
            lines = response.text.strip().split('\n')
            for line in lines:
                # 去除空行和注释行（通常以 # 或 ! 开头）
                clean_line = line.strip()
                if clean_line and not clean_line.startswith(('#', '!')):
                    all_rules.add(clean_line)
            print(f"Successfully processed: {url}")
        else:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while fetching {url}: {e}")

# 将去重后的规则写入新文件
output_filename = "merged_rules.txt"
with open(output_filename, 'w', encoding='utf-8') as f:
    # 排序可以使每次生成的文件内容顺序保持一致，方便追踪变化
    for rule in sorted(list(all_rules)):
        f.write(rule + '\n')

print(f"\nAll rules have been merged and de-duplicated into {output_filename}")
print(f"Total unique rules: {len(all_rules)}")