import os

path = r'E:\000\0000课题组\00低空\低空-知识库\低空-知识库\原始素材\文章'

for f in os.listdir(path):
    if '新疆' in f and '亚克西' in f:
        fpath = os.path.join(path, f)
        print(f"FILE: {f}")
        print(f"SIZE: {os.path.getsize(fpath)} bytes")
        print("=" * 60)
        with open(fpath, 'r', encoding='utf-8') as fh:
            content = fh.read()
        # Skip SVG and Baidu header noise, find actual content
        # Look for article text after frontmatter
        parts = content.split('---')
        if len(parts) >= 3:
            # After second --- is the actual content
            main = parts[2]
            print(main[:8000])
        else:
            print(content[:8000])
        break
