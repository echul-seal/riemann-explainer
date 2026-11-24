from common import *
import mpmath


def zeta_c(s, t):
    return complex(mpmath.zeta(mpmath.mpc(s, t)))


class S2_0(Base):
    def construct(self):
        f = MathTex(r"\zeta(", r"s", r") = 1 + \frac{1}{2^{", r"s", r"}} + \frac{1}{3^{", r"s", r"}} + \frac{1}{4^{", r"s", r"}} + \cdots", font_size=64).shift(UP * 1.8)
        for i in (1, 3, 5, 7):
            f[i].set_color(S_C)
        self.play(Write(f), run_time=2.5)
        self.at('When s is two')
        f2 = MathTex(r"\zeta(2) = 1 + \tfrac14 + \tfrac19 + \tfrac1{16} + \cdots", font_size=50).shift(DOWN * 0.1)
        self.play(Write(f2), run_time=1.5)
        ax = Axes(x_range=[0, 30, 5], y_range=[1, 1.7, 0.1], x_length=8, y_length=2.2, tips=False,
                  axis_config={"color": GREY_D}).shift(DOWN * 2.4)
        ps = np.cumsum(1 / np.arange(1, 31) ** 2)
        dots = VGroup(*[Dot(ax.c2p(i + 1, v), radius=0.05, color=PI_C) for i, v in enumerate(ps)])
        lim = DashedLine(ax.c2p(0, np.pi ** 2 / 6), ax.c2p(30, np.pi ** 2 / 6), color=PR_C)
        ll = MathTex(r"\tfrac{\pi^2}{6}", color=PR_C, font_size=40).next_to(lim, RIGHT)
        self.play(FadeIn(ax), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.08), run_time=2.5)
        self.at('pi squared')
        self.play(Create(lim), Write(ll), run_time=1)
        self.at('When s is one')
        f3 = MathTex(r"\zeta(1) = 1 + \tfrac12 + \tfrac13 + \tfrac14 + \cdots = \infty", font_size=50).move_to(f2)
        self.play(FadeOut(VGroup(ax, dots, lim, ll)), ReplacementTransform(f2, f3), run_time=1.2)
        self.finish()
        self.play(FadeOut(f3), f.animate.to_edge(UP, buff=0.8).scale(0.85), run_time=0.6)


class S2_1(Base):
    def construct(self):
        f = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^s}", font_size=72)
        f[0][1:4].set_color(PI_C)
        f[0][5].set_color(PI_C)
        f[0][6].set_color(S_C)
        f.shift(LEFT * 3.2)
        ex = VGroup(*[MathTex(a, font_size=46) for a in [r"12 = 2^2\cdot 3", r"45 = 3^2\cdot 5", r"98 = 2\cdot 7^2"]]).arrange(DOWN, buff=0.4)
        for e in ex:
            e.set_color(GREY_A)
        self.play(LaggedStart(*[Write(e) for e in ex], lag_ratio=0.4), run_time=2.5)
        self.at('Because of that')
        self.play(FadeOut(ex), run_time=0.5)
        self.play(Write(f), run_time=1.2)
        eq = MathTex("=", font_size=72).next_to(f, RIGHT, buff=0.5)
        p = MathTex(r"\prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}", font_size=72).next_to(eq, RIGHT, buff=0.5)
        p.set_color(PR_C)
        self.at('product over all primes')
        self.play(Write(eq), Write(p), run_time=2)
        self.at('left side never')
        b1 = SurroundingRectangle(f, color=PI_C, buff=0.2)
        self.play(Create(b1), run_time=0.8)
        self.at('right side is')
        b2 = SurroundingRectangle(p, color=PR_C, buff=0.2)
        self.play(ReplacementTransform(b1, b2), run_time=0.8)
        self.at('bridge')
        self.play(FadeOut(b2), Indicate(eq, scale_factor=1.4), run_time=1)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


def plane(xr=(-14, 6, 2), yr=(-5.625, 5.625, 2)):
    return ComplexPlane(x_range=list(xr), y_range=list(yr), x_length=14.222, y_length=8,
                        background_line_style={"stroke_color": GREY_D, "stroke_width": 1, "stroke_opacity": 0.4},
                        axis_config={"stroke_color": GREY_B})


class S2_2(Base):
    def construct(self):
        pl = plane()
        self.add(pl)
        s = MathTex(r"s = \sigma + it", font_size=54).to_corner(UL, buff=0.5)
        s[0][0].set_color(S_C)
        bg = BackgroundRectangle(s, fill_opacity=0.7, buff=0.15)
        self.at('complex number')
        self.play(Create(pl), FadeIn(bg), Write(s), run_time=1.5)
        self.at('only makes sense')
        reg = Rectangle(width=pl.c2p(6, 0)[0] - pl.c2p(1, 0)[0], height=8, fill_color=PI_C, fill_opacity=0.25, stroke_width=0)
        reg.move_to([(pl.c2p(6, 0)[0] + pl.c2p(1, 0)[0]) / 2, 0, 0])
        rl = MathTex(r"\sigma > 1", color=PI_C, font_size=44).move_to(reg).shift(UP * 2.8)
        self.play(FadeIn(reg), Write(rl), run_time=1.2)
        img = ImageMobject(R + '/dcA.png')
        img.height = 8
        img.set_z_index(-1)
        self.at('exactly one way')
        self.play(FadeIn(img), run_time=2.5)
        self.at('blows up')
        pole = pl.n2p(1)
        c = Circle(radius=0.3, color=WHITE).move_to(pole)
        pl1 = MathTex("s=1", font_size=36).next_to(c, UP + RIGHT, buff=0.05)
        self.play(Create(c), FadeIn(pl1), run_time=0.8)
        self.at('analytic continuation')
        ac = Text('analytic continuation', font_size=34).to_edge(DOWN, buff=0.4)
        acb = BackgroundRectangle(ac, fill_opacity=0.7, buff=0.15)
        self.play(FadeOut(reg), FadeOut(rl), FadeIn(acb), Write(ac), run_time=1)
        self.at('hue is its angle')
        self.play(FadeOut(c), FadeOut(pl1), run_time=0.5)
        self.at('Where every color')
        z = Circle(radius=0.28, color=WHITE, stroke_width=4).move_to(pl.n2p(-2))
        self.play(Create(z), run_time=0.8)
        self.play(Indicate(z, color=WHITE), run_time=1)
        self.finish()


class S2_3(Base):
    def construct(self):
        pl = plane()
        img = ImageMobject(R + '/dcA.png')
        img.height = 8
        img.set_z_index(-1)
        self.add(img, pl)
        self.at('minus two')
        tz = VGroup(*[Circle(radius=0.22, color=WHITE, stroke_width=4).move_to(pl.n2p(k)) for k in (-2, -4, -6, -8, -10, -12)])
        self.play(LaggedStart(*[Create(c) for c in tz], lag_ratio=0.3), run_time=2.5)
        self.at('trivial zeros')
        tl = Text('trivial zeros', font_size=34).next_to(pl.n2p(-7), DOWN, buff=0.6)
        tb = BackgroundRectangle(tl, fill_opacity=0.7, buff=0.12)
        self.play(FadeIn(tb), Write(tl), run_time=1)
        self.at('All the others')
        x0, x1 = pl.c2p(0, 0)[0], pl.c2p(1, 0)[0]
        strip = Rectangle(width=x1 - x0, height=8, fill_color=WHITE, fill_opacity=0.22, stroke_color=WHITE, stroke_width=2).move_to([(x0 + x1) / 2, 0, 0])
        self.play(FadeIn(strip), run_time=1.2)
        self.at('critical strip')
        sl = MathTex(r"0 < \sigma < 1", font_size=40).next_to(strip, RIGHT, buff=0.3).shift(UP * 3)
        slb = BackgroundRectangle(sl, fill_opacity=0.7, buff=0.12)
        self.play(FadeIn(slb), Write(sl), run_time=1)
        self.at('center line')
        line = Line(pl.c2p(0.5, -5.625), pl.c2p(0.5, 5.625), color=PR_C, stroke_width=5)
        cl = MathTex(r"\sigma = \tfrac12", color=PR_C, font_size=44).next_to(line, LEFT, buff=0.3).shift(UP * 3)
        clb = BackgroundRectangle(cl, fill_opacity=0.7, buff=0.12)
        self.play(Create(line), FadeIn(clb), Write(cl), run_time=1.5)
        self.finish()


class S2_4(Base):
    def construct(self):
        img = ImageMobject(R + '/dcB.png')
        img.height = 8
        img.to_edge(LEFT, buff=0.6)
        L, Rr = img.get_left()[0], img.get_right()[0]
        B, T = img.get_bottom()[1], img.get_top()[1]

        def p(s, t):
            return np.array([L + (s + 1) / 3 * (Rr - L), B + t / 32 * (T - B), 0])
        line = Line(p(0.5, 0), p(0.5, 32), color=PR_C, stroke_width=3)
        ax0 = Line(p(-1, 0), p(2, 0), color=GREY_B)
        lbl = MathTex(r"\sigma=\tfrac12", color=PR_C, font_size=32).next_to(img, UP, buff=0.1)
        self.add(img, line, ax0)
        self.play(FadeIn(lbl), run_time=0.5)
        zs = ZEROS[:3]
        for k, (w, g) in enumerate(zip(['Fourteen', 'Twenty-one', 'Twenty-five'], zs)):
            self.at(w)
            d = Dot(p(0.5, g), color=WHITE, radius=0.09)
            t = MathTex(r"\tfrac12 + %.2fi" % g, font_size=34).next_to(p(2, g), RIGHT, buff=0.15)
            self.play(FadeIn(d, scale=2), Write(t), run_time=0.8)
        # right: output plane curve
        self.at('Watch what zeta')
        out = ComplexPlane(x_range=[-1.5, 3.5, 1], y_range=[-2, 2, 1], x_length=6.5, y_length=5.2,
                           background_line_style={"stroke_color": GREY_D, "stroke_opacity": 0.4},
                           axis_config={"stroke_color": GREY_B}).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)
        ol = MathTex(r"\zeta(\tfrac12 + it)", font_size=40).next_to(out, UP, buff=0.15)
        ol[0][2:8].set_color(S_C)
        self.play(FadeOut(VGroup(*[m for m in self.mobjects if isinstance(m, MathTex) and m is not lbl])), Create(out), Write(ol), run_time=1.2)
        ts = np.linspace(0, 32, 1400)
        vals = [zeta_c(0.5, t) for t in ts]
        tr = ValueTracker(0)
        def path():
            n = max(2, int(tr.get_value() / 32 * 1400))
            m = VMobject(color=S_C, stroke_width=3)
            m.set_points_as_corners([out.n2p(v) for v in vals[:n]])
            return m
        cur = always_redraw(path)
        mover = always_redraw(lambda: Dot(p(0.5, tr.get_value()), color=S_C, radius=0.07))
        org = Dot(out.n2p(0), color=WHITE, radius=0.06)
        self.add(cur, mover, org)
        rem = self.D() - self.now() - 2.0
        flashes = []
        self.play(tr.animate.set_value(32), run_time=max(rem, 4), rate_func=linear)
        self.at('a zero', off=0.2) if self.tw('a zero') > self.now() else None
        self.play(Flash(org, color=WHITE, flash_radius=0.4), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S2_5(Base):
    def construct(self):
        st = MathTex(r"\zeta(\rho) = 0,\ \ 0<\mathrm{Re}(\rho)<1", r"\ \Longrightarrow\ ", r"\mathrm{Re}(\rho) = \tfrac12", font_size=60)
        st[2].set_color(PR_C)
        t = Text('The Riemann Hypothesis', font_size=44, color=GREY_A).next_to(st, UP, buff=0.9)
        self.play(FadeIn(t), run_time=0.8)
        self.play(Write(st[0]), run_time=1.5)
        self.at('real part')
        self.play(Write(st[1]), Write(st[2]), run_time=1.5)
        self.play(Circumscribe(st[2], color=PR_C), run_time=1)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
