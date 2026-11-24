# The Riemann Hypothesis — script v1

Seal, Nov 24 2026. Target ~10–11 min. Each scene: narration (spoken, exactly as TTS reads it) + visuals.
Facts checked against Seal's Riemann Watch tracker (updated 2026-11-24 13:05Z) and Sutherland's MIT status page.

---

## Scene 1 — The staircase (hook)

VISUALS: number line, primes light up in yellow. Then pi(x) as a blue staircase. Zoom out 100 → 1,000 → 1,000,000; x/ln x in green below it, Li(x) in yellow on top of it. Readout at 10^10.

NARRATION:
Here are the prime numbers. Two, three, five, seven, eleven, thirteen. Numbers with no divisors except one and themselves. Up close, they look random. Sometimes two primes are only two apart. Sometimes there's a gap of hundreds.

But step back, and count them. Pi of x is the number of primes up to x. Every time we pass a prime, the count steps up by one, so pi of x is a staircase. Zoom out to a thousand, then a million, and the staircase smooths into a curve.

In 1896 it was proved that this curve grows like x divided by the natural log of x. That's the prime number theorem. But x over log x runs a little low. Gauss had a better guess: the logarithmic integral, Li of x, the area under one over log t. Li hugs the staircase astonishingly well. Up to ten billion there are about four hundred fifty-five million primes, and Li misses by only about three thousand.

So the primes follow a law. The real question is how far they can stray from it. The Riemann Hypothesis is the answer.

---

## Scene 2 — The zeta function

VISUALS: the series for zeta(s), partial sums for s=2 converging to pi^2/6. Euler product appears below, color-linked: integers (blue) on the left, primes (yellow) on the right. Complex plane; region Re s > 1 shaded, then domain coloring spreads across the plane. Trivial zeros marked at -2, -4, -6. Critical strip shaded, critical line in yellow. First zeros at 14.13, 21.02, 25.01. Then the curve zeta(1/2 + it) drawn in the output plane, spiralling, flashing each pass through the origin.

NARRATION:
To see why, we need a function Riemann studied in 1859: the zeta function. Zeta of s is one, plus one over two to the s, plus one over three to the s, and so on forever. When s is two, this adds up to pi squared over six. When s is one, it's the harmonic series, and it grows without bound.

Euler noticed something wonderful. Every whole number breaks into primes in exactly one way. Because of that, the sum over all whole numbers equals a product over all primes: one over one minus p to the minus s, for every prime p. The left side never mentions primes. The right side is nothing but primes. That equation is the bridge.

Riemann's move was to let s be a complex number, sigma plus i t. The sum only makes sense when the real part, sigma, is bigger than one. But there is exactly one way to extend zeta smoothly to the rest of the plane, except at s equals one, where it blows up. This is called analytic continuation. Here, each point is colored by the value zeta takes there: the hue is its angle, the brightness is its size. Where every color meets at a single point, zeta is zero.

Some zeros are easy to find: at minus two, minus four, minus six, and so on. These are the trivial zeros. All the others live inside this vertical band, where sigma is between zero and one. It's called the critical strip, and its zeros are mirrored around its center line, sigma equals one half.

Riemann computed the first few by hand. Fourteen point one three. Twenty-one point zero two. Twenty-five point zero one. Each one sat on that center line. Watch what zeta does as we walk up the line. Zeta of one half plus i t traces out this looping curve, and every time it passes straight through the origin, that's a zero.

The Riemann Hypothesis says: every nontrivial zero has real part exactly one half.

---

## Scene 3 — Why it matters: the music of the primes

VISUALS: psi(x) staircase (blue). Explicit formula with x in green, the sum over rho in yellow. One wave for the first zero pair, then partial sums with 1, 5, 20, 100 zero pairs rebuilding the staircase. Then a strip diagram: a hypothetical zero off the line at sigma=0.8 and its wave growing like x^0.8 vs the sqrt(x) envelope. Then pi(x) - Li(x) inside a ±sqrt(x) log x envelope. Then primes mod 10 sorted into 4 columns.

NARRATION:
Why would anyone care where the zeros of a function sit? Because the zeros control the primes, exactly.

It's cleanest with a slightly different count, psi of x, which adds up log p for every prime power up to x. It's another staircase, and the prime number theorem says it grows like x. Riemann's idea, made precise by von Mangoldt, is the explicit formula: psi of x equals x, minus a sum over every nontrivial zero rho of x to the rho over rho, minus a couple of small terms.

Each zero, one half plus i gamma, contributes a wave. x to the rho is the square root of x times x to the i gamma, which oscillates in log x with frequency gamma. Start with the smooth line, x. Add the wave from the first zero and its mirror image. Now five zeros. Twenty. A hundred. The waves conspire, and the line sharpens into the staircase, with a jump at every prime power. The zeros are the frequencies of the primes.

The size of the error is set by the real parts. A zero with real part sigma makes a wave that grows like x to the sigma. If every sigma is one half, the primes never stray from Li of x by more than about the square root of x times log x. And that's not just a consequence. Von Koch showed in 1901 that this bound is equivalent to the Riemann Hypothesis. The hypothesis says the primes are as regular as they could possibly be.

It reaches further. Dirichlet L-functions do for primes in arithmetic progressions, like primes ending in one, three, seven or nine, what zeta does for all primes. The Generalized Riemann Hypothesis puts their zeros on the same line, and it says the primes split evenly among those classes, with the same square-root error. Under it, Miller's primality test from 1976 becomes fast and fully deterministic, and many running-time bounds in computational number theory, the kind cryptography leans on, become provable. A huge body of mathematics begins with the words: assume the Riemann Hypothesis.

---

## Scene 4 — Why it's hard

VISUALS: critical strip, a thin zero-free sliver hugging Re s = 1 that narrows as t grows (c / log t). Counter of verified zeros climbing to 10^13, all yellow dots on the line, then the line stretching off to infinity. Plot of Li(x) - pi(x) staying positive, with a "Littlewood: changes sign infinitely often" note. Hilbert–Pólya: zeros as eigenvalues on a vertical axis. Weil: a curve over a finite field, its zeros on its own critical circle. A dotted "F_1" box under Spec Z.

NARRATION:
So why has it resisted for a hundred and sixty-seven years?

Start with what we can prove. In 1896, Hadamard and de la Vallée Poussin showed that no zero sits on the edge of the strip, where sigma equals one. That alone gives the prime number theorem. In 1899, de la Vallée Poussin widened that to a region: no zeros within about a constant over log t of the edge. But look at its shape. As t grows, the zero-free region gets thinner. More than a century of improvements has only shaved slivers near the edge. Nobody can show that even the band where sigma is bigger than point nine nine nine is free of zeros.

Computation won't settle it either. More than ten trillion zeros have been checked, and every one is on the line. But there are infinitely many, and number theory has a history of patterns that break far beyond any computer. Pi of x is below Li of x for every x anyone has ever computed, yet Littlewood proved that it eventually crosses above, and does so infinitely often.

So people looked for a reason the zeros should be on the line. Hilbert and Pólya suggested one. If the heights of the zeros were the eigenvalues of a self-adjoint operator, they would be forced to be real numbers, and that would pin every zero to the line. Nobody has found that operator.

There is one world where the analogue was proved. Curves over finite fields have zeta functions too, and André Weil proved their Riemann hypothesis in the 1940s. Deligne extended it to all such varieties in 1974. Those proofs use geometry: you can take the curve times itself, and count how sub-curves intersect. For the ordinary integers, that geometry is missing. Alain Connes and others have tried to build it, imagining a "field with one element" sitting underneath the integers. It's a deep program, and it hasn't closed the gap.

---

## Scene 5 — 167 years

VISUALS: a horizontal timeline, dates appearing one by one with small icons: Riemann's manuscript page, Hilbert's list, a partial bar filling for the proportion of zeros on the line (Selberg >0, Levinson 1/3, Conrey 2/5), a histogram of zero spacings overlaid with the GUE curve, Clay's 2000.

NARRATION:
Here's the arc. 1859: Riemann, in an eight-page paper, his only one on number theory, states the hypothesis almost in passing, saying it is "very probably" true. 1900: Hilbert puts it on his list of twenty-three problems for the new century. 1914: Hardy proves that infinitely many zeros lie on the line. 1942: Selberg proves that a positive fraction of them do. Levinson pushes that past a third in 1974, and Conrey past two fifths in 1989. In the 1940s, Weil proves the finite-field version.

1972: over tea in Princeton, Hugh Montgomery shows Freeman Dyson his formula for how the zeros repel each other. Dyson recognizes it at once. It's the same statistics as the eigenvalues of large random matrices, the ones physicists use to model the energy levels of heavy nuclei. In the 1980s, Andrew Odlyzko computed zeros near the ten to the twentieth, and their spacings matched the random-matrix prediction with striking precision. 2000: the Clay Mathematics Institute names it one of seven Millennium Problems, with a million-dollar prize.

---

## Scene 6 — November 2026

VISUALS: "Nov 20, 2026". A 4-page note icon, then a wall of 175,187 tiny file squares. A small Lean snippet: `theorem riemann_hypothesis : RiemannHypothesis`. Then the mechanics: a proof term as a tree; a small box labeled kernel checks each node, ticking green. Several kernel boxes side by side (Lean, Lean paranoid, nanoda, lean4lean, con-leche), all green. Statement-match: two copies of the statement side by side, an equals sign. Then a two-column ledger: "verified" vs "understood". End: the critical line with its zeros, camera pulling back into darkness.

NARRATION:
Then, on November twentieth, 2026, Levent Alpöge of Anthropic, working with Claude, posted a four-page note and an archive of Lean code. It claims the Riemann Hypothesis, and the generalized version for Dirichlet L-functions.

Here's what that archive is. Lean is a programming language in which a mathematical statement is a type, and a proof of it is a term of that type. To check a proof, Lean's kernel, a small program, walks through the term and confirms that every step is a valid use of a fixed set of rules. It doesn't judge whether an argument is clever or plausible. It accepts, or it rejects. So the trust rests on three things: that small kernel, the axioms the proof uses, and the statement meaning what we think it means.

This archive is a hundred seventy-five thousand files, about seventeen million lines, exporting to a sixty-one gigabyte proof. It compiles using only Lean's three standard axioms. Kernels written independently, by different people in different languages, accept the full proof, and so do Lean's own kernel and its paranoid mode. The theorem it proves is Mathlib's own definition of the Riemann Hypothesis, written well before any of this, and separate tools confirmed it matches an independently written challenge. On November twenty-first, the Lean and Mathlib communities put out a joint statement certifying both the statement and the proof.

What it isn't, yet: the Clay Institute still lists the problem as unsolved. And there is no human-readable proof. Alpöge estimates that written out in prose, it would run past two hundred fifty thousand pages. The first human guides are appearing, but the furthest along still takes its key inequality from the Lean code on trust. The same day, a separate, all-human attempt was announced: Alessandro Masullo's nine-hundred-forty-page draft. It's now under major revision, with specific problems reported.

So here's where we are. A machine-checked proof says every nontrivial zero lies on the line. If it holds, everything that began with "assume the Riemann Hypothesis" is simply true. And yet nobody can tell you why the zeros line up. For a hundred and sixty-seven years, a proof was how we would come to understand the primes. Now we have the proof. The understanding is still out there.
