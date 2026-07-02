# -*- coding: utf-8 -*-
"""link-lint.py — 知识库内部链接完整性检查
Usage: python _scripts/link-lint.py [--fix] [--quiet]
Exit 1 = broken links found.
"""
import os, re, sys, glob

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIX = '--fix' in sys.argv
QUIET = '--quiet' in sys.argv

file_index = {}
for f in glob.glob(os.path.join(WIKI, '**', '*.md'), recursive=True):
    rel = os.path.relpath(f, WIKI).replace('\\', '/')
    name = os.path.basename(rel)
    if name not in file_index:
        file_index[name] = []
    file_index[name].append(rel)

KB = os.path.join(WIKI, '知识库')
if not os.path.isdir(KB):
    print('WARNING: knowledge base dir not found')
    sys.exit(1)

err, fix = 0, 0
for md in glob.glob(os.path.join(KB, '**', '*.md'), recursive=True):
    rel = os.path.relpath(md, WIKI).replace('\\', '/')
    dname = os.path.dirname(rel)
    
    try:
        with open(md, 'r', encoding='utf-8-sig') as f:
            content = f.read()
    except:
        try:
            with open(md, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            if not QUIET:
                print(f'  SKIP (encoding): {rel}')
            continue
    
    changed = False
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
        target = m.group(2).strip()
        text = m.group(1).strip()
        
        skip = any(target.lower().startswith(p) for p in (
            'http://', 'https://', '#', 'mailto:', 'data:'))
        if skip:
            continue
        
        if target.startswith('/'):
            resolved = target.lstrip('/')
        elif target.startswith('知识库/') or target.startswith('原始素材/'):
            resolved = target
        else:
            resolved = os.path.normpath(os.path.join(dname, target)).replace('\\', '/')
        
        abs_path = os.path.join(WIKI, resolved)
        
        # Check: file exists? file.md exists? target ends with / (dir link)?
        if os.path.isfile(abs_path):
            continue
        if os.path.isfile(abs_path + '.md'):
            continue
        if (resolved.endswith('/') or target.endswith('/')) and os.path.isdir(abs_path):
            continue
        
        # Try auto-fix
        if FIX:
            tname = os.path.basename(target)
            if tname in file_index and not target.startswith('知识库/') and not target.startswith('/'):
                correct = file_index[tname][0]
                old = f'[{text}]({target})'
                new = f'[{text}]({correct})'
                if old in content:
                    content = content.replace(old, new)
                    fix += 1
                    changed = True
                    if not QUIET:
                        print(f'  FIXED: {rel} {target} -> {correct}')
                    continue
        
        err += 1
        if not QUIET:
            print(f'  BROKEN: {rel} -> [{text}]({target})')
    
    if changed:
        with open(md, 'w', encoding='utf-8') as f:
            f.write('\ufeff' + content)

if err > 0:
    if not QUIET:
        print(f'\n=== {err} broken link(s) found ===')
    if FIX and fix > 0:
        print(f'  Fixed: {fix}')
    sys.exit(1)
else:
    if not QUIET:
        print('=== All links OK ===')
    if FIX and fix > 0:
        print(f'  Fixed: {fix}')
    sys.exit(0)
