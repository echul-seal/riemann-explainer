from common import *


class S1_0(Base):
    def construct(self):
        nl = NumberLine(x_range=[0, 60, 5], length=13, include_numbers=True, font_size=24, color=GREY_C).shift(DOWN * 0.3)
        self.play(Create(nl), run_time=1.5)
        dots = VGroup()
        for n in range(2, 61):
            d = Dot(nl.n2p(n) + UP * 0.35, radius=0.06, color=GREY_D)
            d.n = n
            dots.add(d)
        self.add(dots)
        primes = [d for d in dots if d.n in set(PR[:20])]
        self.at('Two')
        first = primes[:6]
        for d in first:
            self.play(d.animate.set_color(PR_C).scale(1.8), run_time=0.35)
        self.at('Numbers with')
        rest = primes[6:]
        self.play(LaggedStart(*[d.animate.set_color(PR_C).scale(1.8) for d in rest], lag_ratio=0.15), run_time=2)
        lbl = MathTex(r"2,\ 3,\ 5,\ 7,\ 11,\ 13,\ \dots", color=PR_C, font_size=48).to_edge(UP, buff=1)
        self.play(Write(lbl), run_time=1.2)
        self.at('Up close')
        self.play(dots.animate.shift(UP * 0.0), run_time=0.1)
        self.at('only two apart')
        tw = VGroup(*[d for d in primes if d.n in (41, 43)])
        b1 = SurroundingRectangle(tw, color=PR_C, buff=0.12)
        self.play(Create(b1), run_time=0.6)
        self.at('gap of hundreds')
        gap = MathTex(r"370{,}261 \;\longrightarrow\; 370{,}373", font_size=40, color=GREY_A)
        gl = cap('111 composites in a row', 26).next_to(gap, DOWN, buff=0.15)
        g = VGroup(gap, gl).next_to(nl, DOWN, buff=0.9)
        self.play(FadeOut(b1), FadeIn(g, shift=UP * 0.2), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S1_1(Base):
    def construct(self):
        ax = Axes(x_range=[0, 100, 10], y_range=[0, 26, 5], x_length=11, y_length=5.5,
                  axis_config={"color": GREY_C, "include_numbers": True, "font_size": 24}).shift(DOWN * 0.3)
        lab = MathTex(r"\pi(x)", color=PI_C, font_size=52).to_corner(UL, buff=0.7)
        sub = cap('number of primes up to x', 26).next_to(lab, RIGHT, buff=0.3)
        self.play(Create(ax), run_time=1.2)
        self.at('Pi of x')
        self.play(Write(lab), FadeIn(sub), run_time=1)
        self.at('Every time')
        st = staircase(ax, PR, 0, 100)
        self.play(Create(st), run_time=4, rate_func=linear)
        self.at('Zoom out')
        ax2 = Axes(x_range=[0, 1000, 100], y_range=[0, 180, 30], x_length=11, y_length=5.5,
                   axis_config={"color": GREY_C, "include_numbers": True, "font_size": 22}).shift(DOWN * 0.3)
        st2 = staircase(ax2, PR, 0, 1000, width=2.5)
        self.play(ReplacementTransform(ax, ax2), ReplacementTransform(st, st2), run_time=2)
        self.at('a million')
        ax3 = Axes(x_range=[0, 1_000_000, 200_000], y_range=[0, 80_000, 20_000], x_length=11, y_length=5.5,
                   axis_config={"color": GREY_C, "include_numbers": False}).shift(DOWN * 0.3)
        xl = VGroup(*[MathTex(s, font_size=26, color=GREY_B).next_to(ax3.c2p(v, 0), DOWN)
                      for v, s in [(200000, r"2{\cdot}10^5"), (600000, r"6{\cdot}10^5"), (1000000, r"10^6")]])
        yl = VGroup(*[MathTex(s, font_size=26, color=GREY_B).next_to(ax3.c2p(0, v), LEFT)
                      for v, s in [(40000, "40{,}000"), (80000, "80{,}000")]])
        xs = np.linspace(2, 1_000_000, 600)
        st3 = curve(ax3, xs, pi_of(xs), PI_C, 3)
        self.play(ReplacementTransform(ax2, ax3), ReplacementTransform(st2, st3), FadeIn(xl), FadeIn(yl), run_time=2.5)
        self.finish()


class S1_2(Base):
    def construct(self):
        ax = Axes(x_range=[0, 1_000_000, 200_000], y_range=[0, 80_000, 20_000], x_length=11, y_length=5.5,
                  axis_config={"color": GREY_C, "include_numbers": False}).shift(DOWN * 0.3)
        xl = VGroup(*[MathTex(s, font_size=26, color=GREY_B).next_to(ax.c2p(v, 0), DOWN)
                      for v, s in [(200000, r"2{\cdot}10^5"), (600000, r"6{\cdot}10^5"), (1000000, r"10^6")]])
        yl = VGroup(*[MathTex(s, font_size=26, color=GREY_B).next_to(ax.c2p(0, v), LEFT)
                      for v, s in [(40000, "40{,}000"), (80000, "80{,}000")]])
        xs = np.linspace(2, 1_000_000, 600)
        st = curve(ax, xs, pi_of(xs), PI_C, 3)
        lab = MathTex(r"\pi(x)", color=PI_C, font_size=52).to_corner(UL, buff=0.7)
        self.add(ax, xl, yl, st, lab)
        self.at('1896')
        xs2 = np.linspace(3, 1_000_000, 400)
        g = curve(ax, xs2, xs2 / np.log(xs2), X_C, 3)
        gl = MathTex(r"\frac{x}{\ln x}", color=X_C, font_size=44).next_to(ax.c2p(1_000_000, 72382), RIGHT, buff=0.15).shift(DOWN * 0.45)
        self.play(Create(g), Write(gl), run_time=2)
        pnt = MathTex(r"\pi(x) \sim \frac{x}{\ln x}", font_size=46).next_to(lab, RIGHT, buff=0.8)
        pnt[0][0:4].set_color(PI_C)
        pnt[0][5:].set_color(X_C)
        self.play(Write(pnt), run_time=1.2)
        self.at('runs a little low')
        self.play(Indicate(g, color=X_C, scale_factor=1.0), run_time=1)
        self.at('Gauss')
        L = curve(ax, xs2, Li(xs2), LI_C, 3)
        Ll = MathTex(r"\mathrm{Li}(x)=\int_2^x \frac{dt}{\ln t}", color=LI_C, font_size=42).to_corner(UR, buff=0.7).shift(DOWN * 1.2)
        self.play(FadeOut(pnt), run_time=0.4)
        self.at('logarithmic integral')
        self.play(Create(L), Write(Ll), run_time=2)
        self.at('hugs')
        self.play(st.animate.set_stroke(width=6), run_time=0.8)
        self.at('Up to ten billion')
        grp = VGroup(ax, xl, yl, st, g, gl, L)
        self.play(grp.animate.set_opacity(0.15), FadeOut(Ll), run_time=0.8)
        t = MathTex(r"x = 10^{10}", font_size=54).shift(UP * 1.6)
        r1 = MathTex(r"\pi(x) = 455{,}052{,}511", color=PI_C, font_size=50).next_to(t, DOWN, buff=0.5)
        r2 = MathTex(r"\mathrm{Li}(x) \approx 455{,}055{,}614", color=LI_C, font_size=50).next_to(r1, DOWN, buff=0.3)
        r3 = MathTex(r"\text{off by } \approx 3{,}100", font_size=46, color=WHITE).next_to(r2, DOWN, buff=0.5)
        r0 = MathTex(r"x/\ln x \approx 434{,}294{,}482", color=X_C, font_size=38).next_to(r3, DOWN, buff=0.5)
        self.play(Write(t), run_time=0.8)
        self.play(FadeIn(r1, shift=UP * 0.2), run_time=0.8)
        self.at('Li misses')
        self.play(FadeIn(r2, shift=UP * 0.2), run_time=0.8)
        self.play(Write(r3), FadeIn(r0), run_time=1)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S1_3(Base):
    def construct(self):
        ax = Axes(x_range=[0, 10, 1], y_range=[-3, 3, 1], x_length=11, y_length=4,
                  axis_config={"color": GREY_D}, tips=False).shift(DOWN * 0.6)
        xs = np.linspace(0.01, 10, 300)
        band = ax.get_area(ax.plot(lambda x: 0.9 * np.sqrt(x) / 3 + 0.05, x_range=[0.01, 10], color=PR_C),
                           bounded_graph=ax.plot(lambda x: -0.9 * np.sqrt(x) / 3 - 0.05, x_range=[0.01, 10]),
                           color=PR_C, opacity=0.18)
        mid = ax.plot(lambda x: 0, x_range=[0, 10], color=LI_C, stroke_width=3)
        rng = np.random.default_rng(3)
        w = np.cumsum(rng.normal(0, 0.09, 300))
        w = w / np.max(np.abs(w)) * 0.8 * np.sqrt(xs) / 3
        err = curve(ax, xs, w, PI_C, 3)
        self.play(Create(mid), run_time=0.8)
        self.play(Create(err), run_time=1.5)
        self.at('how far')
        self.play(FadeIn(band), run_time=1.2)
        self.at('Riemann Hypothesis')
        title = Text('The Riemann Hypothesis', font_size=60, weight=BOLD).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
