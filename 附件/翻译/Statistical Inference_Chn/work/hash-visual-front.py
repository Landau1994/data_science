from pathlib import Path
import hashlib, json
w=Path(__file__).resolve().parent
data={f'page-{i:03d}.png':hashlib.sha256((w/'render-output'/f'page-{i:03d}.png').read_bytes()).hexdigest() for i in range(1,33)}
(w/'final-visual-front-hashes.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print('Recorded hashes for 32 inspected images.')
