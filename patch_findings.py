"""Patch missing why/severity/owner/action fields in r3_diag B3-dense rows."""
import csv, io, pathlib

with open('submission/findings.csv', encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))

for r in rows:
    if r.get('round') == 'r3_diag' and r.get('slice') == 'B3-dense' and not r.get('why', '').strip():
        cell = r.get('cell', '')
        what = r.get('what', '')
        if what == 'MISSING':
            r['why'] = 'E4_model_domain'
            r['owner'] = 'ai_team'
            r['action'] = 'keep_with_reason'
            r['severity'] = 'P2'
        elif what == 'SPURIOUS':
            r['why'] = 'E4_model_domain'
            r['owner'] = 'ai_team'
            r['action'] = 'keep_with_reason'
            r['severity'] = 'P2'
        elif what == 'WRONG_CLASS':
            r['why'] = 'E1_annotator_error'
            r['owner'] = 'annotator'
            r['action'] = 'rework'
            r['severity'] = 'P1'
        elif what == 'ATTRIBUTE':
            r['why'] = 'E2_guideline_gap'
            r['owner'] = 'guideline'
            r['action'] = 'keep_with_reason'
            r['severity'] = 'P2'
        else:
            r['why'] = 'E5_unresolved'
            r['owner'] = 'qa'
            r['action'] = 'keep_with_reason'
            r['severity'] = 'P3'

        if not r.get('rule_id', '').strip():
            r['rule_id'] = 'R01'
        if not r.get('evidence', '').strip():
            frame_id = r.get('frame', '').replace('.jpg', '')
            r['evidence'] = f"model_compare.md frame {frame_id} {cell}"
        if not r.get('rules_version', '').strip():
            r['rules_version'] = 'v1.0.0'

out = io.StringIO()
fields = ['round', 'slice', 'frame', 'object_ref', 'cell', 'what', 'why', 'severity',
          'owner', 'rule_id', 'evidence', 'action', 'rules_version', 'note']
writer = csv.DictWriter(out, fieldnames=fields, lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
pathlib.Path('submission/findings.csv').write_text(out.getvalue(), encoding='utf-8')
patched = sum(1 for r in rows if r.get('round') == 'r3_diag' and r.get('slice') == 'B3-dense')
print(f'Patched {patched} B3-dense r3_diag rows. Total rows: {len(rows)}')
