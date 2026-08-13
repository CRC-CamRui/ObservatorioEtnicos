#!/usr/bin/env python3
"""
Genera la trenza del hero como SVG.

Tres hebras siguiendo x = CX + A*sin(2*pi*y/L + phi), con las fases
separadas 120 grados. La profundidad de cada hebra en cada punto es
cos(2*pi*y/L + phi).

CONSTRUCCION: UNA MASCARA POR HEBRA

Cada hebra se dibuja como UN SOLO trazo continuo. El entrelazado se
resuelve con una mascara por hebra: donde otra hebra pasa por delante, la
mascara tiene un agujero negro con la forma de esa otra hebra engrosada.
El excedente de grosor (HALO menos STROKE) es la separacion visible entre
hebras.

Se llego aqui despues de descartar dos construcciones que fallan:

1. Partir cada hebra en segmentos cortos y pintar debajo de cada uno un
   halo del color del fondo. El halo es mas ancho que la hebra, asi que
   muerde lateralmente al segmento vecino de su PROPIA hebra y deja
   muescas. Afinar los segmentos no lo arregla: en la zona inclinada de la
   onda dos segmentos consecutivos se separan en X mas rapido de lo que la
   hebra alcanza a repintar.

2. Recortar bandas de altura L/6 (el orden de profundidad de tres cosenos
   desfasados 120 grados solo cambia cada L/6) y dibujar la hebra completa
   dentro de cada banda. Elimina las muescas, pero deja costuras
   horizontales: dos recortes contiguos que comparten borde no suman
   cobertura completa al componerse. Con cobertura 0.5 a cada lado el
   resultado es 0.75 de color y 0.25 de fondo, y aparece una linea clara.
   Solapar las bandas tampoco sirve, porque entonces el halo de la banda
   siguiente repinta la anterior.

Con mascaras no hay costura posible: la hebra es un unico trazo y nunca se
recorta contra si misma. Ademas la trenza deja de depender del color de
fondo, porque ya no hay halos pintados del color del papel.
"""
import math

W, H = 260, 1020
AMP = 100.0
LAM = 240.0          # longitud de onda
CX = W / 2
STROKE = 42
HALO = STROKE + 9    # el excedente es la separacion visible entre hebras
MARGIN = HALO        # cuanto se extiende la curva fuera de su banda

PHASES = [0.0, 2 * math.pi / 3, 4 * math.pi / 3]
VARS = ["var(--strand-a)", "var(--strand-b)", "var(--strand-c)"]

TOP, BOT = 30.0, H - 30.0
BAND = LAM / 6.0     # el orden de profundidad es constante dentro de L/6


def x_at(y, phi):
    return CX + AMP * math.sin(2 * math.pi * y / LAM + phi)


def depth_at(y, phi):
    return math.cos(2 * math.pi * y / LAM + phi)


def sample(ya, yb, phi, step=4.0):
    n = max(2, int(math.ceil((yb - ya) / step)))
    pts = []
    for j in range(n + 1):
        y = ya + (yb - ya) * j / n
        pts.append((x_at(y, phi), y))
    return "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)


bands = []
y = TOP
while y < BOT - 0.01:
    y2 = min(y + BAND, BOT)
    bands.append((y, y2))
    y = y2

out = []
out.append(
    f'<svg class="braid" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
    f'fill="none" xmlns="http://www.w3.org/2000/svg" role="img" '
    f'aria-label="Tres hebras entrelazadas en una trenza, una por cada eje '
    f'tematico del Observatorio." preserveAspectRatio="xMidYMid meet">'
)

FADE = 90.0          # los extremos se disuelven en vez de cortarse en seco

out.append('  <defs>')

# Degradados para disolver los dos extremos de la trenza
out.append(
    f'    <linearGradient id="tbfT" gradientUnits="userSpaceOnUse" '
    f'x1="0" y1="{TOP:.1f}" x2="0" y2="{TOP + FADE:.1f}">'
    f'<stop offset="0" stop-color="#000"/>'
    f'<stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>'
)
out.append(
    f'    <linearGradient id="tbfB" gradientUnits="userSpaceOnUse" '
    f'x1="0" y1="{BOT:.1f}" x2="0" y2="{BOT - FADE:.1f}">'
    f'<stop offset="0" stop-color="#000"/>'
    f'<stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>'
)

# Un recorte por banda, usado solo dentro de las mascaras
for i, (y0, y1) in enumerate(bands):
    out.append(
        f'    <clipPath id="tbc{i}"><rect x="-30" y="{y0:.1f}" '
        f'width="{W + 60}" height="{y1 - y0:.1f}"/></clipPath>'
    )

# Una mascara por hebra: blanco visible, negro donde otra hebra pasa delante
for s in range(3):
    out.append(f'    <mask id="tbm{s}" maskUnits="userSpaceOnUse" '
               f'x="-30" y="-30" width="{W + 60}" height="{H + 60}">')
    out.append(f'      <rect x="-30" y="-30" width="{W + 60}" '
               f'height="{H + 60}" fill="#fff"/>')
    out.append('      <g fill="none" stroke="#000" '
               f'stroke-width="{HALO}" stroke-linecap="butt" '
               'stroke-linejoin="round">')
    for i, (y0, y1) in enumerate(bands):
        ymid = (y0 + y1) / 2.0
        delante = [
            t for t in range(3)
            if t != s and depth_at(ymid, PHASES[t]) > depth_at(ymid, PHASES[s])
        ]
        if not delante:
            continue
        out.append(f'        <g clip-path="url(#tbc{i})">')
        for t in delante:
            d = sample(y0 - MARGIN, y1 + MARGIN, PHASES[t])
            out.append(f'          <path d="{d}"/>')
        out.append('        </g>')
    out.append('      </g>')
    # Van al final: oscurecen la mascara y disuelven los remates
    out.append(f'      <rect x="-30" y="{TOP - 30:.1f}" width="{W + 60}" '
               f'height="{FADE + 30:.1f}" fill="url(#tbfT)"/>')
    out.append(f'      <rect x="-30" y="{BOT - FADE:.1f}" width="{W + 60}" '
               f'height="{FADE + 30:.1f}" fill="url(#tbfB)"/>')
    out.append('    </mask>')

out.append('  </defs>')

# Las tres hebras, cada una un unico trazo continuo
out.append(f'  <g fill="none" stroke-width="{STROKE}" '
           'stroke-linecap="round" stroke-linejoin="round">')
for s in range(3):
    d = sample(TOP, BOT, PHASES[s], step=3.0)
    out.append(
        f'    <path class="braid-strand braid-s{s}" d="{d}" '
        f'stroke="{VARS[s]}" mask="url(#tbm{s})"/>'
    )
out.append('  </g>')
out.append('</svg>')

svg = "\n".join(out)
with open("/tmp/trenzas/braid.svg.frag", "w", encoding="utf-8") as f:
    f.write(svg)

print(f"bandas: {len(bands)}  hebras: 3  bytes: {len(svg)}")
