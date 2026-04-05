import requests
import re

def convert():
    source_url = "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/proxy-list.txt"
    output_file = "proxy_list.sorl"
    
    try:
        response = requests.get(source_url)
        response.raise_for_status()
        lines = response.text.splitlines()

        sorl_content = ["[SwitchyOmega Conditions]"]
        
        for line in lines:
            line = line.strip()
            # 跳过空行和注释
            if not line or line.startswith("#"):
                continue
            
            # 1. 处理 full: 开头的（精确匹配）
            if line.startswith("full:"):
                domain = line.replace("full:", "")
                sorl_content.append(domain)
            
            # 2. 处理 regexp: 开头的
            # SwitchyOmega 的正则语法与 V2Ray 差异巨大，建议跳过或者按需手动处理
            elif line.startswith("regexp:"):
                # 这里选择跳过，因为直接转换通常会导致 SwitchyOmega 报错或性能极差
                continue
            
            # 3. 处理 domain: 开头或普通域名（匹配子域名）
            else:
                domain = line.replace("domain:", "")
                # 转换成 SwitchyOmega 的通配符格式
                sorl_content.append(f"*.{domain}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(sorl_content))
            
        print(f"转换成功！共处理 {len(sorl_content)-1} 条规则。")

    except Exception as e:
        print(f"转换失败: {e}")

if __name__ == "__main__":
    convert()
