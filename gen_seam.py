#!/usr/bin/env python3
"""
Genera la costura horizontal: la regla de tres hebras que separa el hero
fotografico del cuerpo del documento. Se usa UNA sola vez en la pagina.

Misma construccion por mascaras que gen_braid.py (ver alli el razonamiento
completo sobre por que no sirven ni los segmentos con halo ni las bandas
recortadas), con los ejes cambiados: aqui la trenza avanza en X y ondula
en Y.

El isotipo de la marca ya es un tejido, asi que esto es deliberadamente
subordinado: poca amplitud, trazo fino, altura pequena. No debe competir
con el logo.

Salida: seam.svg.frag, que se inyecta en index.html en el marcador
<div class="seam-wrap">.
"""
import math

W, H = 1400, 60
AMP, LAM = 17.0, 140.0     # amplitud y longitud de onda
CY = H / 2
STROKE, EXTRA = 14, 5      # EXTRA es la separacion visible entre hebras
HALO = STROKE + EXTRA
PHASES = [0.0, 2 * math.pi / 3, 4 * math.pi / 3]
VARS = ["var(--strand-a)", "var(--strand-b)", "var(--strand-c)"]
BAND = LAM / 6             # el orden de profundidad es constante en L/6

y_at = lambda x, p: CY + AMP * math.sin(2 * math.pi * x / LAM + p)
d_at = lambda x, p: math.cos(2 * math.pi * x / LAM + p)


def samp(a, b, p, step):
    n = max(2, int(math.ceil((b - a) / step)))
    return "M " + " L ".join(
        f"{a+(b-a)*j/n:.0f} {y_at(a+(b-a)*j/n, p):.1f}" for j in range(n + 1))


bands = []
x = 0.0
while x < W - 0.01:
    x2 = min(x + BAND, W)
    bands.append((x, x2))
    x = x2

o = [f'<svg class="seam" viewBox="0 0 {W} {H}" preserveAspectRatio="none" '
     f'fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">',
     '<defs>']
for i, (a, b) in enumerate(bands):
    o.append(f'<clipPath id="sb{i}"><rect x="{a:.0f}" y="-20" '
             f'width="{b-a:.0f}" height="{H+40}"/></clipPath>')
for s in range(3):
    o.append(f'<mask id="sm{s}" maskUnits="userSpaceOnUse" x="-20" y="-20" '
             f'width="{W+40}" height="{H+40}">')
    o.append(f'<rect x="-20" y="-20" width="{W+40}" height="{H+40}" fill="#fff"/>')
    o.append(f'<g fill="none" stroke="#000" stroke-width="{HALO}" stroke-linecap="butt">')
    for i, (a, b) in enumerate(bands):
        xm = (a + b) / 2
        front = [t for t in range(3)
                 if t != s and d_at(xm, PHASES[t]) > d_at(xm, PHASES[s])]
        if not front:
            continue
        o.append(f'<g clip-path="url(#sb{i})">')
        for t in front:
            o.append(f'<path d="{samp(a-HALO, b+HALO, PHASES[t], 9)}"/>')
        o.append('</g>')
    o.append('</g></mask>')
o.append('</defs>')
o.append(f'<g fill="none" stroke-width="{STROKE}" stroke-linecap="round">')
for s in range(3):
    o.append(f'<path d="{samp(0, W, PHASES[s], 7)}" stroke="{VARS[s]}" '
             f'mask="url(#sm{s})"/>')
o.append('</g></svg>')

svg = "".join(o)
with open("/tmp/trenzas/seam.svg.frag", "w", encoding="utf-8") as f:
    f.write(svg)
print(f"costura: {len(svg)//1024} KB, {len(bands)} bandas")
