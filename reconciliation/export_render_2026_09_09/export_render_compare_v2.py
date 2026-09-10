from __future__ import annotations
import hashlib, json, re
from pathlib import Path

TARGETS = [
    'Sim Code phase correction',
    'DISTEL THEORY / DT RECURSIVE CONVERGENCE SIMULATION PACK',
    'black_hole', 'Hawking', 'accessibility', 'propulsion_4d_gates'
]
TEXT_EXT = {'.json','.jsonl','.txt','.md','.html','.py','.csv','.gdoc'}

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def scan_file(path):
    if path.suffix.lower() not in TEXT_EXT:
        return None
    hits = []
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            for line_no, line in enumerate(f, 1):
                matched = [t for t in TARGETS if t.lower() in line.lower()]
                if matched:
                    hits.append({'line': line_no, 'targets': matched, 'excerpt': line[:1000].rstrip()})
                    if len(hits) >= 50:
                        break
    except Exception as e:
        return {'error': f'{type(e).__name__}: {e}'}
    if not hits:
        return None
    st = path.stat()
    return {'size_bytes': st.st_size, 'sha256': sha256(path), 'matches': hits}

def scan_root(label, root):
    root = Path(root)
    rec = {'label': label, 'root': str(root), 'exists': root.exists(), 'files': []}
    if not root.exists():
        return rec
    paths = [root] if root.is_file() else (p for p in root.rglob('*') if p.is_file())
    for p in paths:
        found = scan_file(p)
        if found:
            rec['files'].append({'path': str(p), **found})
    return rec

ROOTS = [
    ('EXPORT_1_GPT_CONVERSATIONS', r'G:\My Drive\TJ\Ai Folder\My Own AI Build\Private personal AI Folder\GPT Conversations'),
    ('EXPORT_2_2026_05_15', r'G:\My Drive\TJ\Ai Folder\My Own AI Build\Private personal AI Folder\TJ GPT DATA EXPORT 05_15_2026'),
    ('EXPORT_3_2026_06_04', r'G:\My Drive\TJ\Ai Folder\My Own AI Build\Private personal AI Folder\TJ GPT DATA EXPORT 06_04_2026'),
    ('EXPORT_4_RESTRICTED_RENDER', r'G:\My Drive\TJ\Ai Folder\My Own AI Build\07_Restricted_Proprietary_and_Creator_Only\01_Raw_ChatGPT_Conversation_History_and_Project_Record'),
]

def main():
    report = {'targets': TARGETS, 'roots': []}
    for label, root in ROOTS:
        print('SCANNING', label, flush=True)
        report['roots'].append(scan_root(label, root))
    out = Path(__file__).with_name('cross_export_match_report.json')
    out.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print('WROTE', out)
    for root in report['roots']:
        print(root['label'], 'matched_files=', len(root['files']))

if __name__ == '__main__':
    main()
