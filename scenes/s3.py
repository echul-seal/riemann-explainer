from common import *


def vm(n):
    """von Mangoldt: log p if n = p^k."""
    for p in PR:
        if p > n:
            return 0.0
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return float(np.log(p)) if m == 1 else 0.0
    return 0.0


JUMPS = [(n, vm(n)) for n in range(2, 51) if vm(n) > 0]


def psi_stair(ax, x1=50, color=PI_C, width=3):
    pts = [ax.c2p(1, 0)]
    c = 0
    for n, w in JUMPS:
        if n > x1:
            break
        pts.append(ax.c2p(n, c))
        c += w
        pts.append(ax.c2p(n, c))
    pts.append(ax.c2p(x1, c))
    m = VMobject(color=color, stroke_width=width)
    m.set_points_as_corners(pts)
    return m


XS = np.linspace(1.5, 50, 1500)


def explicit(N):
    x = XS
    y = x - np.log(2 * np.pi) - 0.5 * np.log(1 - x ** -2.0)
    for g in ZEROS[:N]:
        rho = 0.5 + 1j * g
        y = y - 2 * np.real(x ** rho / rho)
    return y


def axes50():
    return Axes(x_range=[0, 50, 10], y_range=[0, 55, 10], x_length=11.5, y_length=5.6,
                axis_config={"color": GREY_C, "include_numbers": True, "font_size": 22}).shift(DOWN * 0.6)


class S3_0(Base):
    def construct(self):
        q = Text('Why do the zeros matter?', font_size=48)
        self.play(Write(q), run_time=1.5)
        self.at('control the primes')
        self.play(q.animate.set_color(PR_C), run_time=0.8)
        self.finish()
        self.play(FadeOut(q), run_time=0.4)


class S3_1(Base):
    def construct(self):
        ax = axes50()
        lab = MathTex(r"\psi(x) = \sum_{p^k \le x} \ln p", font_size=46, color=PI_C).to_corner(UL, buff=0.5)
        self.play(Create(ax), Write(lab), run_time=1.5)
        st = psi_stair(ax)
        self.at('another staircase')
        self.play(Create(st), run_time=2.5, rate_func=linear)
        self.at('grows like x')
        ln = ax.plot(lambda x: x, x_range=[1, 50], color=X_C, stroke_width=3)
        self.play(Create(ln), run_time=1.2)
        self.at('explicit formula')
        self.play(FadeOut(lab), VGroup(ax, st, ln).animate.set_opacity(0.25), run_time=0.8)
        f = MathTex(r"\psi(x)", r"=", r"x", r"-", r"\sum_{\rho}", r"\frac{x^{\rho}}{\rho}", r"-\ln 2\pi - \tfrac12\ln(1-x^{-2})", font_size=56).shift(UP * 0.4)
        f[0].set_color(PI_C)
        f[2].set_color(X_C)
        f[4].set_color(PR_C)
        f[5].set_color(PR_C)
        f[6].set_color(GREY_B)
        self.play(Write(f), run_time=2.5)
        self.at('every nontrivial zero')
        self.play(Circumscribe(VGroup(f[4], f[5]), color=PR_C), run_time=1.2)
        self.at('small terms')
        self.play(Indicate(f[6], color=GREY_A), run_time=1)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S3_2(Base):
    def construct(self):
        ax = axes50()
        st = psi_stair(ax, color=PI_C, width=2).set_opacity(0.35)
        self.add(ax, st)
        w = MathTex(r"x^{\rho} = \sqrt{x}\cdot x^{i\gamma} = \sqrt{x}\, e^{i\gamma \ln x}", font_size=44).to_corner(UL, buff=0.4)
        w.set_color_by_tex(r"\gamma", PR_C)
        self.at('contributes a wave')
        self.play(Write(w), run_time=2)
        self.at('Start with')
        cur = curve(ax, XS, explicit(0), X_C, 3)
        self.play(Create(cur), run_time=1)
        x = XS
        g = ZEROS[0]
        rho = 0.5 + 1j * g
        wave = -2 * np.real(x ** rho / rho)
        wv = curve(ax, XS, wave + 5, PR_C, 2)
        nlab = MathTex(r"N = 0", font_size=44).to_corner(UR, buff=0.5)
        self.add(nlab)
        self.at('first zero')
        self.play(Create(wv), run_time=1.2)
        n1 = MathTex(r"N = 1", font_size=44).move_to(nlab)
        self.play(Transform(cur, curve(ax, XS, explicit(1), X_C, 3)), FadeOut(wv), Transform(nlab, n1), run_time=1.5)
        for word, N in [('five', 5), ('Twenty', 20), ('A hundred', 100)]:
            self.at(word)
            self.play(Transform(cur, curve(ax, XS, explicit(N), X_C, 3)),
                      Transform(nlab, MathTex(r"N = %d" % N, font_size=44).move_to(nlab)), run_time=1.2)
        self.at('conspire')
        for N in (300, 1000):
            self.play(Transform(cur, curve(ax, XS, explicit(N), X_C, 3)),
                      Transform(nlab, MathTex(r"N = %d" % N, font_size=44).move_to(nlab)), run_time=1.5)
        self.at('jump at every')
        self.play(st.animate.set_opacity(0.9), run_time=1)
        tags = VGroup(*[MathTex(str(n), font_size=22, color=PR_C).next_to(ax.c2p(n, 0), UP, buff=0.15) for n, _ in JUMPS if n in (7, 8, 9, 11, 13, 16)])
        self.play(FadeIn(tags), run_time=0.8)
        self.at('frequencies')
        fr = Text('zeros = frequencies of the primes', font_size=34, color=PR_C).to_edge(DOWN, buff=0.15)
        self.play(Write(fr), run_time=1.2)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S3_3(Base):
    def construct(self):
        ax = Axes(x_range=[0, 100, 20], y_range=[-40, 40, 20], x_length=11, y_length=5, tips=False,
                  axis_config={"color": GREY_D}).shift(DOWN * 0.5)
        h = MathTex(r"\rho = \sigma + i\gamma \ \Rightarrow\ |x^{\rho}| = x^{\sigma}", font_size=46).to_edge(UP, buff=0.5)
        self.play(Write(h), Create(ax), run_time=1.5)
        env = ax.plot(lambda x: x ** 0.5, x_range=[0.1, 100], color=PR_C)
        env2 = ax.plot(lambda x: -x ** 0.5, x_range=[0.1, 100], color=PR_C)
        el = MathTex(r"\pm x^{1/2}", color=PR_C, font_size=38).next_to(ax.c2p(100, 10), RIGHT)
        self.at('grows like')
        bad = ax.plot(lambda x: x ** 0.8 * np.cos(14 * np.log(x + 1)), x_range=[0.1, 100], color=RED)
        bl = MathTex(r"x^{0.8}", color=RED, font_size=38).next_to(ax.c2p(100, 38), RIGHT)
        self.play(Create(env), Create(env2), Write(el), run_time=1.5)
        self.play(Create(bad), Write(bl), run_time=2)
        self.at('If every sigma')
        self.play(FadeOut(bad), FadeOut(bl), run_time=0.6)
        self.play(FadeOut(VGroup(ax, env, env2, el)), run_time=0.6)
        b = MathTex(r"|\pi(x) - \mathrm{Li}(x)|", r"\le", r"C\sqrt{x}\,\ln x", font_size=60)
        b[0].set_color(PI_C)
        b[2].set_color(PR_C)
        self.play(Write(b), run_time=2)
        self.at('Von Koch')
        eqv = MathTex(r"\Longleftrightarrow\ \text{RH}", font_size=60).next_to(b, DOWN, buff=0.7)
        vk = Text('von Koch, 1901', font_size=28, color=GREY_B).next_to(eqv, DOWN, buff=0.3)
        self.play(Write(eqv), FadeIn(vk), run_time=1.5)
        self.at('as regular')
        self.play(Circumscribe(b, color=PR_C), run_time=1.5)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


class S3_4(Base):
    def construct(self):
        cols = VGroup()
        cnt = {1: [], 3: [], 7: [], 9: []}
        for p in PR:
            if p > 10 and p < 400 and p % 10 in cnt:
                cnt[p % 10].append(p)
        heads = VGroup(*[MathTex(r"\dots%d" % d, font_size=44, color=PR_C) for d in (1, 3, 7, 9)]).arrange(RIGHT, buff=2.2).to_edge(UP, buff=0.8)
        self.play(FadeIn(heads), run_time=1)
        self.at('primes ending')
        nums = VGroup()
        for d, hd in zip((1, 3, 7, 9), heads):
            col = VGroup(*[MathTex(str(p), font_size=28) for p in cnt[d][:12]]).arrange(DOWN, buff=0.12).next_to(hd, DOWN, buff=0.3)
            nums.add(col)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in nums], lag_ratio=0.25), run_time=2)
        self.at('Generalized')
        g = Text('GRH', font_size=40, color=PR_C).to_edge(DOWN, buff=1.3)
        self.play(Write(g), run_time=0.8)
        self.at('split evenly')
        tot = {d: int(np.sum((PR < 1_000_000) & (PR % 10 == d))) for d in (1, 3, 7, 9)}
        cts = VGroup(*[MathTex(r"%s" % format(tot[d], ',').replace(',', '{,}'), font_size=34, color=PI_C).next_to(hd, DOWN, buff=0.3) for d, hd in zip((1, 3, 7, 9), heads)])
        sub = Text('primes below one million in each class', font_size=26, color=GREY_B).next_to(cts, DOWN, buff=0.4)
        self.play(FadeOut(nums), FadeIn(cts), FadeIn(sub), run_time=1.2)
        self.at('Miller')
        self.play(FadeOut(VGroup(heads, cts, sub, g)), run_time=0.6)
        items = VGroup(
            Text('Miller primality test (1976): deterministic, fast', font_size=32),
            Text('provable running times in computational number theory', font_size=32),
            Text('"Assume the Riemann Hypothesis..."', font_size=32, slant=ITALIC, color=PR_C),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(FadeIn(items[0], shift=RIGHT * 0.3), run_time=0.8)
        self.at('running-time')
        self.play(FadeIn(items[1], shift=RIGHT * 0.3), run_time=0.8)
        self.at('huge body')
        self.play(FadeIn(items[2], shift=RIGHT * 0.3), run_time=0.8)
        self.finish()
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
