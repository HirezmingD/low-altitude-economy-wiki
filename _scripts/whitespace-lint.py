# -*- coding: utf-8 -*-
"""whitespace-lint.py — 正文空白行规范检查

规则：正文中连续 3 个及以上空行（\\n\\n\\n+）→ 压缩为 1 个空行（\\n\\n）
Frontmatter（第一对 --- 之间）不受此规则约束。

Usage: python _scripts/whitespace-lint.py [--fix] [--quiet]
Exit 1 = violations found (or fixed).
"""
import os, re, sys

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIX = '--fix' in sys.argv
QUIET = '--quiet' in sys.argv

violations = []

for dirpath, dirnames, filenames in os.walk(WIKI):
    for fn in filenames:
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(dirpath, fn)
        rel = os.path.relpath(fp, WIKI).replace('\\', '/')

        with open(fp, 'rb') as f:
            raw = f.read()
        has_bom = raw.startswith(b'\xef\xbb\xbf')
        if has_bom:
            raw = raw[3:]

        text = raw.decode('utf-8', errors='replace')
        text_norm = text.replace('\r\n', '\n').replace('\r', '\n')

        # Split frontmatter from body
        if text_norm.startswith('---\n'):
            idx = text_norm.find('\n---', 4)
            if idx != -1:
                body = text_norm[idx + 4:]
            else:
                body = text_norm
        else:
            body = text_norm

        # Find 3+ consecutive newlines
        matches = list(re.finditer(r'\n{3,}', body))
        if not matches:
            continue

        if FIX:
            body_fixed = re.sub(r'\n{3,}', '\n\n', body)
            if text_norm.startswith('---\n') and text_norm.find('\n---', 4) != -1:
                idx = text_norm.find('\n---', 4)
                result = text_norm[:idx + 4] + body_fixed
            else:
                result = body_fixed

            result = result.replace('\n', '\r\n')
            out = result.encode('utf-8')
            if has_bom:
                out = b'\xef\xbb\xbf' + out

            with open(fp, 'wb') as f:
                f.write(out)

        for m in matches:
            line_num = body[:m.start()].count('\n') + 1
            blank_count = len(m.group())
            violations.append((rel, line_num, blank_count))

if violations and not QUIET:
    print(f'共 {len(violations)} 处正文多余空行:')
    for rel, line, count in violations:
        print(f'  {rel}:L{line} (连续{count}个空行)')
    if FIX:
        print('全部已修复。')
    else:
        print('运行 python _scripts/whitespace-lint.py --fix 自动修复。')

if violations:
    sys.exit(1)
else:
    if not QUIET:
        print('空白行规范检查通过。')
    sys.exit(0)
