import os

path = r'E:\000\0000课题组\00低空\低空-知识库\低空-知识库\原始素材\文章'

# Chengdu article
for f in os.listdir(path):
    if '构建低空空域管理' in f:
        fpath = os.path.join(path, f)
        with open(fpath, 'r', encoding='utf-8') as fh:
            content = fh.read()
        print('=== 成都大会 ===')
        print(content[:6000])
        print('=== END ===')
        print()
        break

# Zhu Keli article
for f in os.listdir(path):
    if '专访湾区' in f:
        fpath = os.path.join(path, f)
        with open(fpath, 'r', encoding='utf-8') as fh:
            content = fh.read()
        print('=== 朱克力 ===')
        print(content[:6000])
        print('=== END ===')
        print()
        break
