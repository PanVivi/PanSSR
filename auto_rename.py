# Clash配置自动重命名脚本 (无额外依赖版本)
import re
import sys

def rename_proxies_in_clash_config_simple(config_file, output_file=None):
    """简单的Clash配置重命名器，不需要yaml模块"""

    # 重命名规则
    rename_rules = [
        # 日本节点 - 优先匹配c28s4
        (r'name:\s*["\']([^"\']*?c28s4[^"\']*?)["\']', r'name: "🇯🇵 JP-01"'),
        # 其他日本节点
        (r'name:\s*["\']([^"\']*?(?:日本|JP|Japan|东京|大阪)[^"\']*?)["\']', r'name: "🇯🇵 JP"'),

        # 美国节点 - 按c28s编号匹配
        (r'name:\s*["\']([^"\']*?c28s1[^"\']*?)["\']', r'name: "🇺🇲 US-01"'),
        (r'name:\s*["\']([^"\']*?c28s2[^"\']*?)["\']', r'name: "🇺🇲 US-02"'),
        (r'name:\s*["\']([^"\']*?c28s3[^"\']*?)["\']', r'name: "🇺🇲 US-03"'),
        (r'name:\s*["\']([^"\']*?c28s5[^"\']*?)["\']', r'name: "🇺🇲 US-05"'),
        (r'name:\s*["\']([^"\']*?c28s801[^"\']*?)["\']', r'name: "🇺🇲 US-801"'),
        # 其他美国节点
        (r'name:\s*["\']([^"\']*?(?:美国|US|United States)[^"\']*?)["\']', r'name: "🇺🇲 US"'),
    ]

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        renamed_count = 0

        # 应用重命名规则
        for pattern, replacement in rename_rules:
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, replacement, content)
                renamed_count += len(matches)

        # 如果有重命名，写入文件
        if content != original_content:
            output = output_file or config_file
            with open(output, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f'重命名完成！已处理 {renamed_count} 个节点')
            return True
        else:
            print('未找到需要重命名的节点')
            return False

    except Exception as e:
        print(f'处理失败: {e}')
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: python auto_rename.py <config.yaml> [output.yaml]')
        print('示例: python auto_rename.py config.yaml')
        print('      python auto_rename.py config.yaml renamed.yaml')
        sys.exit(1)

    config_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    rename_proxies_in_clash_config_simple(config_file, output_file)
