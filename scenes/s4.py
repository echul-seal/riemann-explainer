from common import *


def strip_axes():
    return Axes(x_range=[-0.5, 1.5, 0.5], y_range=[0, 100, 20], x_length=6, y_length=6.1, tips=False,
                axis_config={"color": GREY_C, "include_numbers": True, "font_size": 22}).shift(LEFT * 3 + DOWN * 0.3)


class S4_0(Base):
    def construct(self):
        q = MathTex(r"1859 \to 2026", font_size=72)
        self.play(Write(q), run_time=1.5)
        self.finish()
        self.play(FadeOut(q), run_time=0.4)


class S4_1(Base):
    def construct(self):
        ax = strip_axes()
        s0 = ax.c2p(0, 0); s1 = ax.c2p(1, 100)
        strip = Rectangle(width=s1[0] - s0[0], height=s1[1] - s0[1], fill_color=WHITE, fill_opacity=0.12, stroke_color=WHITE, stroke_width=2).move_to((np.array(s0) + np.array(s1)) / 2)
        line = Line(ax.c2p(0.5, 0), ax.c2p(0.5, 100), color=PR_C, stroke_width=4)
        self.play(Create(ax), FadeIn(strip), Create(line), run_time=1.5)
        zs = VGroup(*[Dot(ax.c2p(0.5, g), radius=0.05, color=PR_C) for g in ZEROS[:29]])
        self.add(zs)
        self.at('edge of the strip')
        edge = Line(ax.c2p(1, 0), ax.c2p(1, 100), color=GREEN, stroke_width=6)
        el = MathTex(r"\sigma = 1", color=GREEN, font_size=40).next_to(edge, UP, buff=0.15)
        self.play(Create(edge), Write(el), run_time=1.2)
        hv = Text('Hadamard, de la Vallée Poussin 1896', font_size=26, color=GREY_B).to_edge(RIGHT, buff=0.5).shift(UP * 2.5)
        self.play(FadeIn(hv), run_time=0.8)
        self.at('prime number theorem')
        pnt = MathTex(r"\Rightarrow\ \pi(x)\sim \frac{x}{\ln x}", font_size=40).next_to(hv, DOWN, buff=0.4)
        self.play(Write(pnt), run_time=1)
        self.at('1899')
        c = 0.35
        ts = np.linspace(2, 100, 200)
        pts = [ax.c2p(1 - c / np.log(t + 3), t) for t in ts] + [ax.c2p(1, 100), ax.c2p(1, 2)]
        reg = Polygon(*pts, fill_color=GREEN, fill_opacity=0.45, stroke_width=0)
        f = MathTex(r"\sigma > 1 - \frac{c}{\ln t}", color=GREEN, font_size=44).next_to(pnt, DOWN, buff=0.6)
        self.play(FadeIn(reg), Write(f), run_time=1.5)
        self.at('look at its shape')
        self.play(Indicate(reg, color=GREEN, scale_factor=1.0), run_time=1.2)
        self.at('More than a century')
        self.play(FadeOut(hv), FadeOut(pnt), run_time=0.5)
        self.at('Nobody can show')
        lim = DashedLine(ax.c2p(0.999, 0), ax.c2p(0.999, 100), color=RED)
        q = MathTex(r"\sigma > 0.999 \ ?", color=RED, font_size=44).next_to(f, DOWN, buff=0.6)
        no = Text('not known to be zero-free', font_size=28, color=RED).next_to(q, DOWN, buff=0.25)
        self.play(Create(lim), Write(q), FadeIn(no), run_time=1.5)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S4_2(Base):
    def construct(self):
        ctr = Integer(0, font_size=72, group_with_commas=True).shift(UP * 1.2)
        lab = Text('zeros checked on the line', font_size=32, color=GREY_B).next_to(ctr, DOWN, buff=0.3)
        self.add(lab)
        tr = ValueTracker(0)
        ctr.add_updater(lambda m: m.set_value(int(10 ** tr.get_value())))
        self.add(ctr)
        self.play(tr.animate.set_value(13), run_time=3.5, rate_func=rate_functions.ease_in_out_sine)
        ctr.clear_updaters()
        big = MathTex(r"10^{13}", font_size=90, color=PR_C).move_to(ctr)
        self.play(ReplacementTransform(ctr, big), run_time=0.6)
        self.at('infinitely many')
        inf = MathTex(r"\text{of } \infty", font_size=60).next_to(big, RIGHT, buff=0.4)
        self.play(Write(inf), run_time=0.8)
        self.at('Pi of x is below')
        self.play(FadeOut(VGroup(big, inf, lab)), run_time=0.5)
        ax = Axes(x_range=[0, 1_000_000, 200_000], y_range=[0, 140, 20], x_length=10, y_length=4.2, tips=False,
                  axis_config={"color": GREY_C}).shift(DOWN * 0.8)
        xs = np.linspace(1000, 1_000_000, 500)
        d = Li(xs) - pi_of(xs)
        c = curve(ax, xs, d, LI_C, 3)
        cl = MathTex(r"\mathrm{Li}(x) - \pi(x) > 0", font_size=46).to_edge(UP, buff=0.7)
        cl[0][0:5].set_color(LI_C)
        cl[0][6:11].set_color(PI_C)
        self.play(Create(ax), Create(c), Write(cl), run_time=2)
        self.at('Littlewood')
        lw = Text('Littlewood, 1914: the sign flips infinitely often', font_size=30, color=RED).next_to(cl, DOWN, buff=0.3)
        fl = Text('first flip: somewhere below 10^317', font_size=26, color=GREY_B).next_to(ax, DOWN, buff=0.35)
        self.play(FadeIn(lw), run_time=1)
        self.play(FadeIn(fl), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S4_3(Base):
    def construct(self):
        ax = NumberLine(x_range=[0, 50, 10], length=6.5, rotation=PI / 2, color=GREY_C, include_numbers=True, font_size=22).shift(LEFT * 3)
        hp = Text('Hilbert–Pólya', font_size=40).to_edge(UP, buff=0.6)
        self.play(Write(hp), Create(ax), run_time=1.2)
        self.at('eigenvalues')
        eig = VGroup(*[Line(ax.n2p(g) + LEFT * 0.3, ax.n2p(g) + RIGHT * 0.3, color=PR_C, stroke_width=4) for g in ZEROS[:10]])
        self.play(LaggedStart(*[Create(e) for e in eig], lag_ratio=0.15), run_time=1.8)
        op = MathTex(r"H = H^{*}", r"\ \Rightarrow\ ", r"H v = \gamma v,\ \ \gamma \in \mathbb{R}", font_size=48).shift(RIGHT * 2.3 + UP * 0.8)
        op[2].set_color(PR_C)
        self.play(Write(op), run_time=1.6)
        self.at('pin every zero')
        r = MathTex(r"\rho = \tfrac12 + i\gamma", color=PR_C, font_size=50).next_to(op, DOWN, buff=0.6)
        self.play(Write(r), run_time=1)
        self.at('Nobody has found')
        q = MathTex(r"H = \ ?", font_size=60, color=RED).next_to(r, DOWN, buff=0.7)
        self.play(Write(q), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S4_4(Base):
    def construct(self):
        lab = MathTex(r"y^2 = x^3 + x + 1 \ \text{ over } \ \mathbb{F}_{13}", font_size=40).to_corner(UL, buff=0.5)
        grid = VGroup()
        pts = VGroup()
        for x in range(13):
            for y in range(13):
                d = Dot([x * 0.32 - 5.6, y * 0.32 - 2.6, 0], radius=0.035, color=GREY_D)
                grid.add(d)
                if (y * y - (x ** 3 + x + 1)) % 13 == 0:
                    pts.add(Dot(d.get_center(), radius=0.07, color=PI_C))
        self.play(Write(lab), FadeIn(grid), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(p, scale=2) for p in pts], lag_ratio=0.08), run_time=1.5)
        self.at('Weil proved')
        w = Text('Weil, 1940s: RH for curves', font_size=32, color=PR_C).shift(RIGHT * 2.8 + UP * 1.5)
        self.play(FadeIn(w), run_time=0.8)
        self.at('Deligne')
        dl = Text('Deligne, 1974: all varieties', font_size=32, color=PR_C).next_to(w, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(FadeIn(dl), run_time=0.8)
        self.at('curve times itself')
        cc = MathTex(r"C \times C", font_size=52).next_to(dl, DOWN, buff=0.6)
        self.play(Write(cc), run_time=1)
        self.at('For the ordinary integers')
        self.play(FadeOut(VGroup(lab, grid, pts, w, dl)), cc.animate.shift(LEFT * 2.8 + UP * 1.6), run_time=1)
        zz = MathTex(r"\mathrm{Spec}\,\mathbb{Z} \times \mathrm{Spec}\,\mathbb{Z}\ \ ?", font_size=52).next_to(cc, DOWN, buff=0.6)
        self.play(Write(zz), run_time=1)
        self.at('Alain Connes')
        f1 = DashedVMobject(Rectangle(width=3.2, height=1.1, color=GREY_B))
        f1t = MathTex(r"\mathbb{F}_1", font_size=54).move_to(f1)
        g = VGroup(f1, f1t).next_to(zz, DOWN, buff=0.8)
        cn = Text('Connes and others', font_size=26, color=GREY_B).next_to(g, DOWN, buff=0.2)
        self.play(Create(f1), Write(f1t), FadeIn(cn), run_time=1.5)
        self.at("hasn't closed")
        self.play(f1.animate.set_color(RED), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
