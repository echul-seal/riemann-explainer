from common import *


def tl_item(year, txt, color=PR_C):
    y = MathTex(year, font_size=40, color=color)
    t = Text(txt, font_size=28)
    return VGroup(y, t).arrange(RIGHT, buff=0.4, aligned_edge=DOWN)


class S5_0(Base):
    def construct(self):
        rows = [
            ('1859', 'Riemann: 8 pages, "very probably" true', '1859'),
            ('1900', 'Hilbert: problem 8 of 23', '1900'),
            ('1914', 'Hardy: infinitely many zeros on the line', '1914'),
            ('1942', 'Selberg: a positive fraction', '1942'),
            ('1974', 'Levinson: more than 1/3', 'Levinson'),
            ('1989', 'Conrey: more than 2/5', 'Conrey'),
            ('1940s', 'Weil: the finite-field version', 'Weil'),
        ]
        items = VGroup(*[tl_item(a, b) for a, b, _ in rows]).arrange(DOWN, buff=0.38, aligned_edge=LEFT).shift(LEFT * 0.5)
        for it, (_, _, w) in zip(items, rows):
            self.at(w)
            self.play(FadeIn(it, shift=RIGHT * 0.3), run_time=0.8)
            if w == 'Levinson':
                bar = VGroup(Rectangle(width=4, height=0.25, color=GREY_C), Rectangle(width=4 / 3, height=0.25, fill_color=PR_C, fill_opacity=0.8, stroke_width=0))
                bar[1].align_to(bar[0], LEFT)
                bar.to_edge(RIGHT, buff=0.6).shift(DOWN * 0.3)
                self.play(FadeIn(bar), run_time=0.5)
            if w == 'Conrey':
                self.play(bar[1].animate.stretch_to_fit_width(4 * 0.4, about_edge=LEFT), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S5_1(Base):
    def construct(self):
        h = tl_item('1972', 'Montgomery and Dyson, tea in Princeton').to_edge(UP, buff=0.5)
        self.play(FadeIn(h), run_time=0.8)
        ax = Axes(x_range=[0, 3, 0.5], y_range=[0, 1.6, 0.5], x_length=9, y_length=4.2, tips=False,
                  axis_config={"color": GREY_C, "include_numbers": True, "font_size": 22}).shift(DOWN * 0.7)
        self.at('repel')
        g = ZEROS[10000:100000]
        d = np.diff(g) * np.log(g[:-1] / (2 * np.pi)) / (2 * np.pi)
        hist, edges = np.histogram(d, bins=30, range=(0, 3), density=True)
        bars = VGroup(*[Rectangle(width=ax.c2p(edges[i + 1], 0)[0] - ax.c2p(edges[i], 0)[0], height=max(1e-3, ax.c2p(0, v)[1] - ax.c2p(0, 0)[1]),
                                  fill_color=PI_C, fill_opacity=0.6, stroke_width=1, stroke_color=PI_C).move_to(ax.c2p((edges[i] + edges[i + 1]) / 2, v / 2))
                        for i, v in enumerate(hist)])
        bl = Text('gaps between zeros', font_size=26, color=PI_C).next_to(ax, DOWN, buff=0.35)
        self.play(Create(ax), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.03), FadeIn(bl), run_time=2)
        self.at('random matrices')
        gue = ax.plot(lambda s: 32 / np.pi ** 2 * s ** 2 * np.exp(-4 * s ** 2 / np.pi), x_range=[0, 3], color=PR_C, stroke_width=4)
        gl = Text('random-matrix prediction', font_size=26, color=PR_C).next_to(ax.c2p(1.6, 1.0), RIGHT)
        self.play(Create(gue), FadeIn(gl), run_time=1.5)
        self.at('Odlyzko')
        o = tl_item('1980s', 'Odlyzko: zeros near 10^20 match it').move_to(h)
        self.play(FadeOut(h, shift=UP * 0.2), FadeIn(o, shift=UP * 0.2), run_time=0.8)
        self.at('2000')
        self.play(FadeOut(VGroup(ax, bars, bl, gue, gl, o)), run_time=0.6)
        c = tl_item('2000', 'Clay: one of seven Millennium Problems')
        m = MathTex(r"\$1{,}000{,}000", font_size=64, color=PR_C).next_to(c, DOWN, buff=0.6)
        self.play(FadeIn(c), run_time=0.8)
        self.at('million-dollar')
        self.play(Write(m), run_time=1)
        self.finish()
        self.play(*[FadeOut(mm) for mm in self.mobjects], run_time=0.5)


class S6_0(Base):
    def construct(self):
        d = Text('November 20, 2026', font_size=52)
        self.play(Write(d), run_time=1.2)
        self.at('Levent')
        n = Text('Levent Alpöge (Anthropic), with Claude', font_size=34, color=GREY_A).next_to(d, DOWN, buff=0.5)
        self.play(FadeIn(n), run_time=0.8)
        self.at('four-page')
        a = VGroup(Text('4-page note', font_size=30), Text('+', font_size=30), Text('Lean 4 archive', font_size=30, color=PI_C)).arrange(RIGHT, buff=0.3).next_to(n, DOWN, buff=0.6)
        self.play(FadeIn(a), run_time=0.8)
        self.at('It claims')
        cl = MathTex(r"\text{RH}\ \ +\ \ \text{GRH for Dirichlet } L\text{-functions}", font_size=46, color=PR_C).next_to(a, DOWN, buff=0.6)
        self.play(Write(cl), run_time=1.2)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S6_1(Base):
    def construct(self):
        self.at('Lean is')
        st = VGroup(Text('statement', font_size=34), MathTex(r"\longleftrightarrow", font_size=44), Text('type', font_size=34, color=PI_C)).arrange(RIGHT, buff=0.4)
        pf = VGroup(Text('proof', font_size=34), MathTex(r"\longleftrightarrow", font_size=44), Text('term of that type', font_size=34, color=PI_C)).arrange(RIGHT, buff=0.4)
        g = VGroup(st, pf).arrange(DOWN, buff=0.4, aligned_edge=LEFT).to_edge(UP, buff=0.8)
        self.play(FadeIn(st), run_time=0.8)
        self.at('a proof of it')
        self.play(FadeIn(pf), run_time=0.8)
        self.at("Lean's kernel")
        k = RoundedRectangle(width=2.6, height=1.3, corner_radius=0.2, color=PR_C).shift(DOWN * 0.8)
        kt = Text('kernel', font_size=32, color=PR_C).move_to(k)
        steps = VGroup(*[Square(0.35, fill_color=GREY_C, fill_opacity=0.6, stroke_width=1) for _ in range(8)]).arrange(RIGHT, buff=0.12).next_to(k, LEFT, buff=0.8)
        self.play(Create(k), Write(kt), FadeIn(steps), run_time=1)
        self.at('every step')
        for s in steps[::-1]:
            self.play(s.animate.move_to(k).set_opacity(0), run_time=0.25)
        self.at('accepts, or')
        ok = Text('✓ accept', font_size=34, color=GREEN).next_to(k, RIGHT, buff=0.8).shift(UP * 0.35)
        no = Text('✗ reject', font_size=34, color=RED).next_to(k, RIGHT, buff=0.8).shift(DOWN * 0.35)
        self.play(FadeIn(ok), FadeIn(no), run_time=0.8)
        self.at('three things')
        self.play(FadeOut(VGroup(g, steps, ok, no, k, kt)), run_time=0.6)
        tr = VGroup(Text('1. the small kernel', font_size=36), Text('2. the axioms used', font_size=36),
                    Text('3. the statement means what we think', font_size=36)).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(FadeIn(tr[0], shift=RIGHT * 0.3), run_time=0.6)
        self.at('the axioms')
        self.play(FadeIn(tr[1], shift=RIGHT * 0.3), run_time=0.6)
        self.at('the statement meaning')
        self.play(FadeIn(tr[2], shift=RIGHT * 0.3), run_time=0.6)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S6_2(Base):
    def construct(self):
        ms = VGroup(
            VGroup(MathTex(r"175{,}187", font_size=56, color=PI_C), Text('files', font_size=26, color=GREY_B)).arrange(DOWN),
            VGroup(MathTex(r"\approx 17\text{M}", font_size=56, color=PI_C), Text('lines', font_size=26, color=GREY_B)).arrange(DOWN),
            VGroup(MathTex(r"61\text{ GB}", font_size=56, color=PI_C), Text('proof export', font_size=26, color=GREY_B)).arrange(DOWN),
        ).arrange(RIGHT, buff=1.4).to_edge(UP, buff=0.7)
        for m, w in zip(ms, ['hundred seventy', 'seventeen', 'sixty-one']):
            self.at(w)
            self.play(FadeIn(m, shift=UP * 0.2), run_time=0.7)
        self.at('three standard axioms')
        ax = Text('only the 3 standard axioms', font_size=30).next_to(ms, DOWN, buff=0.7)
        self.play(FadeIn(ax), run_time=0.7)
        self.at('Kernels written')
        ks = VGroup(*[VGroup(RoundedRectangle(width=2.4, height=0.9, corner_radius=0.15, color=GREEN), Text(t, font_size=24)).arrange(ORIGIN)
                      for t in ['independent', 'independent', "Lean's own", 'paranoid mode']]).arrange(RIGHT, buff=0.35).next_to(ax, DOWN, buff=0.6)
        for kk in ks:
            kk[1].move_to(kk[0])
        self.play(LaggedStart(*[FadeIn(kk) for kk in ks], lag_ratio=0.25), run_time=2)
        self.play(*[kk[0].animate.set_fill(GREEN, 0.25) for kk in ks], run_time=0.8)
        self.at("Mathlib's own")
        st = MathTex(r"\texttt{theorem}\ :\ \texttt{RiemannHypothesis}", font_size=44, color=PR_C).next_to(ks, DOWN, buff=0.7)
        self.play(Write(st), run_time=1.2)
        self.at('November twenty-first')
        n21 = Text('Nov 21: Lean + Mathlib joint statement', font_size=30, color=GREY_A).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(n21), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S6_3(Base):
    def construct(self):
        c = Text('Clay Institute: still listed as unsolved', font_size=34).to_edge(UP, buff=0.8)
        self.play(FadeIn(c), run_time=0.8)
        self.at('no human-readable')
        b = MathTex(r"> 250{,}000\ \text{pages of prose}", font_size=56, color=PR_C)
        self.at('two hundred fifty')
        self.play(Write(b), run_time=1.2)
        self.at('first human guides')
        g = Text('first human guides: key inequality still taken from the Lean code', font_size=26, color=GREY_B).next_to(b, DOWN, buff=0.6)
        self.play(FadeIn(g), run_time=0.8)
        self.at('Masullo')
        m = Text('Masullo: 940-page human draft, under major revision', font_size=28, color=GREY_A).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(m), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(mm) for mm in self.mobjects], run_time=0.5)


class S6_4(Base):
    def construct(self):
        ax = Axes(x_range=[-0.5, 1.5, 0.5], y_range=[0, 60, 10], x_length=4, y_length=7, tips=False, axis_config={"color": GREY_D}).shift(LEFT * 4)
        line = Line(ax.c2p(0.5, 0), ax.c2p(0.5, 60), color=PR_C, stroke_width=4)
        zs = VGroup(*[Dot(ax.c2p(0.5, g), radius=0.06, color=PR_C) for g in ZEROS[:16]])
        self.play(Create(ax), Create(line), run_time=1)
        self.at('every nontrivial')
        self.play(LaggedStart(*[FadeIn(z, scale=2) for z in zs], lag_ratio=0.1), run_time=2)
        self.at('nobody can tell')
        w = Text('verified', font_size=44, color=GREEN).shift(RIGHT * 2 + UP * 1)
        u = Text('understood ?', font_size=44, color=GREY_B).next_to(w, DOWN, buff=0.6)
        self.play(FadeIn(w), run_time=0.8)
        self.play(FadeIn(u), run_time=0.8)
        self.at('The understanding')
        self.play(u.animate.set_color(WHITE), Indicate(u), run_time=1.2)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)
