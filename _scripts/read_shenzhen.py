import os

path = r'E:\000\0000课题组\00低空\低空-知识库\低空-知识库\原始素材\文章'

for f in os.listdir(path):
    if '深圳探路' in f:
        fpath = os.path.join(path, f)
        print(f"FILE: {f}")
        print(f"SIZE: {os.path.getsize(fpath)} bytes")
        print("=" * 60)
        with open(fpath, 'r', encoding='utf-8') as fh:
            content = fh.read()
        # Split on --- to get content after frontmatter
        parts = content.split('---')
        if len(parts) >= 3:
            main = parts[2]
            print(main[:10000])
        else:
            print(content[:10000])
        break
