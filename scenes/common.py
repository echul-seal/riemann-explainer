from manim import *
import numpy as np, json
from scipy.special import expi

R = '/home/sprite/rh'
config.background_color = "#0d0f14"
config.frame_rate = 30
config.pixel_width = 1920
config.pixel_height = 1080

DUR = {}
for l in open(R + '/audio/dur2.txt'):
    a, b = l.split()
    DUR[a.replace('.dec.mp3', '')] = float(b)
NAR = json.load(open(R + '/narration.json'))
ZEROS = np.loadtxt(R + '/zeros1')

PI_C = BLUE          # pi(x), integers
PR_C = YELLOW        # primes, zeros
X_C = GREEN          # x/log x, smooth main term
LI_C = YELLOW_D      # Li(x)
S_C = TEAL           # the variable s
DIM = GREY_B


def sieve(n):
    s = np.ones(n + 1, bool)
    s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


PR = sieve(1_100_000)


def pi_of(x):
    return np.searchsorted(PR, x, side='right')


def li(x):
    return expi(np.log(x))


def Li(x):
    return li(x) - li(2.0)


def cap(t, size=30, color=DIM):
    return Text(t, font_size=size, color=color)


def staircase(ax, xs_jump, x0, x1, color=PI_C, width=3):
    """Step graph that jumps by 1 at each value in xs_jump, drawn from x0 to x1."""
    pts = [ax.c2p(x0, 0)]
    c = 0
    for p in xs_jump:
        if p < x0 or p > x1:
            continue
        pts.append(ax.c2p(p, c))
        c += 1
        pts.append(ax.c2p(p, c))
    pts.append(ax.c2p(x1, c))
    m = VMobject(color=color, stroke_width=width)
    m.set_points_as_corners(pts)
    return m


def curve(ax, xs, ys, color, width=3):
    m = VMobject(color=color, stroke_width=width)
    m.set_points_smoothly([ax.c2p(a, b) for a, b in zip(xs, ys)]) if len(xs) < 400 else \
        m.set_points_as_corners([ax.c2p(a, b) for a, b in zip(xs, ys)])
    return m


class Base(Scene):
    PAD = 0.5

    @property
    def key(self):
        return type(self).__name__.lower()

    def D(self):
        return DUR[self.key]

    def now(self):
        return self.renderer.time

    def text(self):
        s, i = self.key.split('_')
        return NAR[s][int(i)]

    def tw(self, word, nth=1):
        txt = self.text()
        i = -1
        for _ in range(nth):
            i = txt.find(word, i + 1)
        if i < 0:
            raise ValueError('word not in narration: ' + word)
        return i / len(txt) * self.D()

    def at(self, word, off=0.0, nth=1):
        self.until(self.tw(word, nth) + off)

    def until(self, t):
        dt = t - self.now()
        if dt > 0.04:
            self.wait(dt)

    def finish(self):
        self.until(self.D() + self.PAD)
