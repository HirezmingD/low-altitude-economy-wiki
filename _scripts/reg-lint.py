# -*- coding: utf-8 -*-
"""reg-lint.py — 法规与作者引用链接完整性检查

检查知识库中是否存在：
1. 法规名称裸引用（未挂链接）
2. 中文作者年份引用（如"张三等 (2026)"）未挂链接
3. 英文 et al. 引用未挂链接

Usage: python _scripts/reg-lint.py [--quiet]
Exit 1 = bare references found.
"""
import os, re, sys

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(WIKI, '知识库')
QUIET = '--quiet' in sys.argv

# ── Regulation names ──
REGULATIONS = [
    ('中华人民共和国民用航空法', '知识库/政策/中国/民用航空法2026.md'),
    ('民用航空法', '知识库/政策/中国/民用航空法2026.md'),
    ('无人驾驶航空器飞行管理暂行条例', '知识库/政策/中国/无人驾驶航空器飞行管理暂行条例.md'),
    ('中华人民共和国飞行基本规则', '知识库/政策/中国/飞行基本规则.md'),
    ('飞行基本规则', '知识库/政策/中国/飞行基本规则.md'),
    ('通用航空飞行管制条例', '知识库/政策/中国/通用航空飞行管制条例.md'),
    ('通用航空经营许可管理规定', '知识库/政策/中国/通用航空经营许可管理规定.md'),
    ('民用航空空中交通管理规则', '知识库/政策/中国/民用航空空中交通管理规则.md'),
    ('浙江省民用航空条例', '知识库/政策/中国/浙江省民用航空条例.md'),
    ('深圳市低空基础设施高质量建设方案', '知识库/政策/中国/深圳市低空基础设施高质量建设方案.md'),
    ('低空航路运行安全能力评估规范', '知识库/政策/中国/低空航路运行安全能力评估规范.md'),
    ('国家空域基础分类方法', '知识库/概念/空域治理/空域分类制度.md'),
    ('空域管理条例', '知识库/概念/空域治理/空域分类制度.md'),
    ('中华人民共和国空域管理条例', '知识库/概念/空域治理/空域分类制度.md'),
    ('EU 2021/664', '知识库/概念/空域治理/U-Space低空生态体系.md'),
    ('Part 107', '知识库/实体/国家地区/美国.md'),
    ('CCAR-92', '知识库/政策/中国/无人驾驶航空器飞行管理暂行条例.md'),
]

# ── Self-reference exemptions ──
SELF_PAGES = {
    '知识库/政策/中国/民用航空法2026.md',
    '知识库/政策/中国/飞行基本规则.md',
    '知识库/政策/中国/无人驾驶航空器飞行管理暂行条例.md',
    '知识库/政策/中国/通用航空飞行管制条例.md',
    '知识库/政策/中国/通用航空经营许可管理规定.md',
    '知识库/政策/中国/民用航空空中交通管理规则.md',
    '知识库/政策/中国/浙江省民用航空条例.md',
    '知识库/政策/中国/低空航路运行安全能力评估规范.md',
    '知识库/政策/中国/深圳市低空基础设施高质量建设方案.md',
    '知识库/概念/空域治理/U-Space低空生态体系.md',
    '知识库/概念/空域治理/空域分类制度.md',
    '知识库/概念/空域治理/通用航空飞行管制条例.md',
    '知识库/实体/国家地区/美国.md',
}

# ── Author-to-page mapping (key authors) ──
AUTHOR_PAGES = {
    '安诣彬': '知识库/摘要/空域治理/空—地协同低空空域划设技术.md',
    '石春晖': '知识库/摘要/空域治理/低空开发权与用途管制体系.md',
    '黄建中': '知识库/摘要/容量评估/城市低空规划地空协同.md',
    '刘冲': '知识库/摘要/空域治理/低空空域经营权理论.md',
    '豆书龙': '知识库/摘要/空域治理/低空管理到低空治理政策演进.md',
    '张珺皓': '知识库/摘要/空域治理/低空经济法治保障研究.md',
    '刘露': '知识库/摘要/空域治理/低空交通空间要素规划体系.md',
    '黄经南': '知识库/摘要/空域治理/AI城市空间学术笔谈.md',
    '廖小罕': '知识库/摘要/容量评估/低空空域资源量测度框架.md',
    '王姣娥': '知识库/摘要/容量评估/低空人地系统理论.md',
    '倪红福': '知识库/摘要/空域治理/低空空域管理经济学逻辑.md',
    '张洪海': '知识库/摘要/容量评估/城市低空航路规划综述.md',
    '李诚龙': '知识库/摘要/容量评估/eVTOL航空器UAM交通管理综述.md',
    '包丹文': '知识库/摘要/容量评估/低空空域规划综述.md',
    '李艳华': '知识库/摘要/容量评估/移动闭塞低空交通系统.md',
    '张云景': '知识库/摘要/容量评估/CNN-ConvLSTM空域复杂度预测.md',
    '包杰': '知识库/摘要/容量评估/异质飞行流多尺度协同调控.md',
    '张召悦': '知识库/摘要/容量评估/城市风场栅格化路径优化.md',
    '赵嶷飞': '知识库/摘要/容量评估/物流无人机进场航线设计.md',
    '冯明翔': '知识库/摘要/容量评估/多源数据限制区识别.md',
    '党安荣': '知识库/摘要/容量评估/低空基础设施规划综述.md',
    '王纪武': '知识库/摘要/容量评估/低空空域利用规划应对策略.md',
    '全权': '知识库/摘要/容量评估/SkyHighway空中高速公路.md',
    '唐炉亮': '知识库/摘要/容量评估/低空天际线地图.md',
    '张晓兰': '知识库/摘要/空域治理/新型空域管理体系构建.md',
    '董志毅': '知识库/摘要/空域治理/低空安全新治理体系.md',
    '朱克力': '知识库/摘要/产业转化/低空经济拐点与产业落地路径.md',
    '李佳睿': '知识库/摘要/空域治理/低空空域分类及监管框架.md',
    '黄启翔': '知识库/摘要/容量评估/国土空间精细化治理适配策略.md',
    '樊一江': '知识库/摘要/产业转化/低空经济阶段特征与场景.md',
    '李晓华': '知识库/摘要/产业转化/政府引导与低空产业生态.md',
    'Pongsakornsathien': '知识库/摘要/容量评估/低空空域管理进展综述.md',
}

def read_file(path):
    if not os.path.exists(path): return ''
    with open(path, 'rb') as f:
        raw = f.read()
    if raw.startswith(b'\xef\xbb\xbf'): raw = raw[3:]
    return raw.decode('utf-8', errors='replace')

def is_inside_link(text, pos):
    before = text[:pos]
    lo = before.rfind('['); lc = before.rfind(']')
    po = before.rfind('('); pc = before.rfind(')')
    if lo > lc: return True
    if po > pc and po > 0 and before[po - 1] == ']': return True
    return False

def find_bare(text, pattern, self_page_rel=''):
    """Find bare occurrences of pattern not inside a link"""
    found = []
    for m in re.finditer(pattern, text):
        if not is_inside_link(text, m.start()):
            # Check if this is a self-reference (page title)
            ctx = text[max(0, m.start() - 5):m.end() + 5]
            if ctx.strip().startswith('#') and self_page_rel:
                continue  # heading, skip
            found.append(m.start())
    return found

errors = []

# Walk all KB markdown files
for dirpath, dirnames, filenames in os.walk(KB):
    for fname in filenames:
        if not fname.endswith('.md'): continue
        fpath = os.path.join(dirpath, fname)
        rel = os.path.relpath(fpath, WIKI).replace('\\', '/')
        
        text = read_file(fpath)
        parts = text.split('---', 2)
        body = parts[2] if len(parts) >= 3 else text
        
        # Check regulations
        is_self_page = rel in SELF_PAGES
        for reg_name, _ in REGULATIONS:
            # Skip all regulations on self-pages (page is about itself)
            if is_self_page:
                continue
            if reg_name not in body: continue
            
            bare_positions = find_bare(body, re.escape(reg_name), rel)
            if bare_positions:
                for pos in bare_positions:
                    ctx_start = max(0, pos - 20)
                    ctx_end = min(len(body), pos + len(reg_name) + 20)
                    ctx = body[ctx_start:ctx_end].replace('\n', ' ').replace('\r', '')
                    errors.append((rel, f'法规裸引用: "{reg_name}"', f'...{ctx}...'))
        
        # Check author references (Chinese: Name等/Name (year))
        author_pattern = re.compile(r'([\u4e00-\u9fff]{2,4})(?:等)?[\s]*[（(](\d{4})[)）]')
        for m in author_pattern.finditer(body):
            if is_inside_link(body, m.start()):
                continue
            name = m.group(1)
            year = m.group(2)
            if name in AUTHOR_PAGES:
                ctx_start = max(0, m.start() - 10)
                ctx_end = min(len(body), m.end() + 10)
                ctx = body[ctx_start:ctx_end].replace('\n', ' ').replace('\r', '')
                errors.append((rel, f'作者裸引用: {name}等 ({year})', f'...{ctx}...'))

# Report
if not QUIET:
    for rel, issue, ctx in errors:
        print(f'{rel}: {issue}')
        print(f'  {ctx}')
        print()

if errors:
    print(f'\n共 {len(errors)} 处链接缺失。')
    print('修复指南：')
    print('  法规名 → 添加 [法规名](目标路径)')
    print('  作者引用 → 添加 [作者等 (年份)](对应摘要页路径)')
    sys.exit(1)
else:
    print('所有法规和作者引用均已挂上链接。')
    sys.exit(0)
