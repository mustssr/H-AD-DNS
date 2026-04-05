import requests

def convert():
    source_url = "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/proxy-list.txt"
    output_file = "proxy_list.sorl"
    
    try:
        # 获取原始列表
        response = requests.get(source_url)
        response.raise_for_status()
        lines = response.text.splitlines()

        # 构建 SwitchyOmega 格式
        # 第一行必须是 [SwitchyOmega Conditions]
        sorl_content = ["[SwitchyOmega Conditions]"]
        
        for line in lines:
            line = line.strip()
            # 跳过注释和空行
            if line and not line.startswith("#"):
                # SwitchyOmega 规则格式：*.domain.com 或 domain.com
                # 这里我们保持原样或根据需要添加通配符
                sorl_content.append(f"*{line}")

        # 写入根目录
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(sorl_content))
            
        print(f"转换成功，已生成 {output_file}")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    convert()
