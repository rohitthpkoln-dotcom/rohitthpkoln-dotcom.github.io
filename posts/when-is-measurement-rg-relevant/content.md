---
title: "When Is a Measurement RG-Relevant?"
date: 2026-05-17
excerpt: "A step-by-step guide to the R to 1 replica trick, the measurement Harris criterion, and the 2D Ising spin and energy examples."
tags: replica theory, measurement, renormalization group, Ising CFT
---

## Overview

This note answers a simple question:

\[
\text{If I weakly measure a local operator at a critical point, is that measurement RG-relevant?}
\]

The short answer is:

\[
y_\gamma=d-2\Delta_{\mathcal{O}},
\]

where:

- \(d\) is the spacetime dimension of the Euclidean critical theory,
- \(\mathcal{O}\) is the operator being measured,
- \(\Delta_{\mathcal{O}}\) is the scaling dimension of that operator,
- \(\gamma\) is the measurement strength.

Thus:

\[
y_\gamma>0 \Rightarrow \text{relevant},
\]

\[
y_\gamma=0 \Rightarrow \text{marginal},
\]

\[
y_\gamma<0 \Rightarrow \text{irrelevant}.
\]

A PDF version is also available here:

[Download the step-by-step PDF](../../assets/ordinary_nishimori_step_by_step.pdf)

## Replica trick for measurements

Start with an unperturbed CFT with action

\[
S_*[\phi].
\]

Suppose we weakly measure a local operator \(\phi(x)\) with a Gaussian detector. The measurement outcome is \(m(x)\), and the likelihood is

\[
P[m|\phi]\propto
\exp\left[
-\frac{1}{2\Delta}
\int d^d x\,
\left(m(x)-\phi(x)\right)^2
\right].
\]

The important point is that measurement outcomes are not quenched disorder. They are sampled with their Born/Bayesian probability. This changes the replica limit.

For quenched disorder:

\[
R\to0.
\]

For measurement/Bayesian conditioning:

\[
R\to1.
\]

The \(R\) replicas all couple to the same outcome field \(m(x)\).

## Gaussian integration over the outcome

At one spacetime point, suppress \(x\) and write

\[
A=\sum_{a=1}^R \phi^{(a)}.
\]

Now expand the square:

\[
\sum_{a=1}^R \left(m-\phi^{(a)}\right)^2
=
\sum_{a=1}^R
\left[
m^2-2m\phi^{(a)}+\phi^{(a)2}
\right].
\]

Therefore

\[
\sum_{a=1}^R \left(m-\phi^{(a)}\right)^2
=
Rm^2-2m\sum_a\phi^{(a)}+\sum_a\phi^{(a)2}.
\]

Using \(A=\sum_a\phi^{(a)}\),

\[
\sum_{a=1}^R \left(m-\phi^{(a)}\right)^2
=
Rm^2-2mA+\sum_a\phi^{(a)2}.
\]

Complete the square:

\[
Rm^2-2mA
=
R\left(m-\frac{A}{R}\right)^2-\frac{A^2}{R}.
\]

So

\[
\sum_{a=1}^R \left(m-\phi^{(a)}\right)^2
=
R\left(m-\frac{A}{R}\right)^2
-\frac{A^2}{R}
+\sum_a\phi^{(a)2}.
\]

Now integrate over \(m\):

\[
\int dm\,
\exp\left[
-\frac{1}{2\Delta}
\sum_{a=1}^R
\left(m-\phi^{(a)}\right)^2
\right]
\]

\[
\propto
\exp\left[
-\frac{1}{2\Delta}\sum_a\phi^{(a)2}
+\frac{1}{2\Delta R}
\left(\sum_a\phi^{(a)}\right)^2
\right].
\]

Next expand the remaining square:

\[
\left(\sum_a\phi^{(a)}\right)^2
=
\sum_a\phi^{(a)2}
+2\sum_{a<b}\phi^{(a)}\phi^{(b)}.
\]

Substitute:

\[
-\frac{1}{2\Delta}\sum_a\phi^{(a)2}
+\frac{1}{2\Delta R}
\left[
\sum_a\phi^{(a)2}
+2\sum_{a<b}\phi^{(a)}\phi^{(b)}
\right].
\]

Put the diagonal terms over a common denominator:

\[
-\frac{R}{2\Delta R}\sum_a\phi^{(a)2}
+\frac{1}{2\Delta R}\sum_a\phi^{(a)2}
+\frac{1}{\Delta R}\sum_{a<b}\phi^{(a)}\phi^{(b)}.
\]

Therefore

\[
-\frac{R-1}{2\Delta R}\sum_a\phi^{(a)2}
+\frac{1}{\Delta R}\sum_{a<b}\phi^{(a)}\phi^{(b)}.
\]

Reading this as \(e^{-\delta S}\), the replicated action gains

\[
\delta S
=
-\frac{1}{\Delta R}
\int d^d x
\sum_{a<b}
\phi^{(a)}(x)\phi^{(b)}(x)
+
\frac{R-1}{2\Delta R}
\int d^d x
\sum_a\phi^{(a)2}(x).
\]

The second term has a prefactor \(R-1\), so it vanishes in the measurement limit \(R\to1\). The important term is the off-diagonal replica coupling:

\[
\delta S_{\text{meas}}
=
-\gamma
\int d^d x
\sum_{a\ne b}
\phi^{(a)}(x)\phi^{(b)}(x).
\]

## Power counting

Let the measured operator have scaling dimension

\[
\Delta_\phi.
\]

Under a scale transformation \(x\to bx\),

\[
d^d x \to b^d d^d x.
\]

Also

\[
\phi(x)\to b^{-\Delta_\phi}\phi(x/b).
\]

Therefore

\[
\phi^{(a)}(x)\phi^{(b)}(x)
\to
b^{-\Delta_\phi}b^{-\Delta_\phi}
\phi^{(a)}(x/b)\phi^{(b)}(x/b).
\]

So

\[
\phi^{(a)}(x)\phi^{(b)}(x)
\to
b^{-2\Delta_\phi}
\phi^{(a)}(x/b)\phi^{(b)}(x/b).
\]

The full perturbation scales as

\[
\int d^d x\,\phi^{(a)}\phi^{(b)}
\to
b^d b^{-2\Delta_\phi}
\int d^d x\,\phi^{(a)}\phi^{(b)}.
\]

Thus

\[
\int d^d x\,\phi^{(a)}\phi^{(b)}
\to
b^{d-2\Delta_\phi}
\int d^d x\,\phi^{(a)}\phi^{(b)}.
\]

So the RG eigenvalue of the measurement strength is

\[
y_\gamma=d-2\Delta_\phi.
\]

## Measurement Harris criterion

The measurement is relevant if

\[
y_\gamma>0.
\]

Using \(y_\gamma=d-2\Delta_\phi\), this means

\[
d-2\Delta_\phi>0.
\]

Equivalently,

\[
2\Delta_\phi<d.
\]

So:

\[
2\Delta_\phi<d
\Rightarrow
\text{relevant}.
\]

\[
2\Delta_\phi=d
\Rightarrow
\text{marginal}.
\]

\[
2\Delta_\phi>d
\Rightarrow
\text{irrelevant}.
\]

This is the same tree-level form as the Harris criterion for disorder, but the replica limit is different:

\[
R\to1
\quad\text{for measurement},
\]

while

\[
R\to0
\quad\text{for quenched disorder}.
\]

## Free scalar: measuring \(\phi\)

For the free massless scalar,

\[
S_*=\frac12\int d^d x\,(\partial\phi)^2.
\]

The action is dimensionless. The dimensions are

\[
[d^d x]=-d,
\]

\[
[\partial]=1,
\]

\[
[\phi]=\Delta_\phi.
\]

The integrand has dimension

\[
[(\partial\phi)^2]
=
2[\partial]+2[\phi].
\]

So

\[
[(\partial\phi)^2]
=
2+2\Delta_\phi.
\]

For the action to be dimensionless:

\[
[d^d x]+[(\partial\phi)^2]=0.
\]

Substitute:

\[
-d+(2+2\Delta_\phi)=0.
\]

Therefore

\[
2+2\Delta_\phi=d.
\]

Subtract \(2\) from both sides:

\[
2\Delta_\phi=d-2.
\]

Divide by \(2\):

\[
\Delta_\phi=\frac{d-2}{2}.
\]

Now use

\[
y_\gamma=d-2\Delta_\phi.
\]

Substitute \(\Delta_\phi=(d-2)/2\):

\[
y_\gamma
=
d-2\left(\frac{d-2}{2}\right).
\]

Cancel the factor of \(2\):

\[
y_\gamma
=
d-(d-2).
\]

Distribute the minus sign:

\[
y_\gamma
=
d-d+2.
\]

Therefore

\[
y_\gamma=2.
\]

So weak measurement of a free scalar field \(\phi\) is strongly relevant.

## Wilson-Fisher: measuring \(\phi^2\)

Now measure the energy operator

\[
\varepsilon\sim\phi^2
\]

at the Wilson-Fisher fixed point in

\[
d=4-\epsilon.
\]

The important mistake to avoid is using the free-field answer \(\Delta_{\phi^2}=d-2\). At Wilson-Fisher, \(\phi^2\) has an anomalous dimension.

The energy scaling dimension is

\[
\Delta_\varepsilon=d-\frac{1}{\nu}.
\]

At one loop,

\[
\nu=\frac12+\frac{\epsilon}{12}+O(\epsilon^2).
\]

Rewrite this as

\[
\nu=\frac12\left(1+\frac{\epsilon}{6}\right)+O(\epsilon^2).
\]

Invert:

\[
\frac1\nu
=
\frac{2}{1+\epsilon/6}+O(\epsilon^2).
\]

Use

\[
\frac{1}{1+x}=1-x+O(x^2).
\]

With \(x=\epsilon/6\),

\[
\frac1\nu
=
2\left(1-\frac{\epsilon}{6}\right)+O(\epsilon^2).
\]

So

\[
\frac1\nu
=
2-\frac{\epsilon}{3}+O(\epsilon^2).
\]

Now compute \(\Delta_\varepsilon\):

\[
\Delta_\varepsilon
=
d-\frac1\nu.
\]

Substitute

\[
d=4-\epsilon
\]

and

\[
\frac1\nu=2-\frac{\epsilon}{3}+O(\epsilon^2).
\]

Then

\[
\Delta_\varepsilon
=
(4-\epsilon)-\left(2-\frac{\epsilon}{3}\right)+O(\epsilon^2).
\]

Expand:

\[
\Delta_\varepsilon
=
4-\epsilon-2+\frac{\epsilon}{3}+O(\epsilon^2).
\]

Combine constants:

\[
4-2=2.
\]

Combine \(\epsilon\) terms:

\[
-\epsilon+\frac{\epsilon}{3}
=
-\frac{2\epsilon}{3}.
\]

Therefore

\[
\Delta_\varepsilon
=
2-\frac{2\epsilon}{3}+O(\epsilon^2).
\]

Now compute the measurement RG eigenvalue:

\[
y_\gamma=d-2\Delta_\varepsilon.
\]

Substitute:

\[
y_\gamma
=
(4-\epsilon)-2\left(2-\frac{2\epsilon}{3}\right)+O(\epsilon^2).
\]

Multiply out:

\[
2\left(2-\frac{2\epsilon}{3}\right)
=
4-\frac{4\epsilon}{3}.
\]

So

\[
y_\gamma
=
4-\epsilon-\left(4-\frac{4\epsilon}{3}\right)+O(\epsilon^2).
\]

Expand:

\[
y_\gamma
=
4-\epsilon-4+\frac{4\epsilon}{3}+O(\epsilon^2).
\]

Cancel \(4-4\):

\[
y_\gamma
=
-\epsilon+\frac{4\epsilon}{3}+O(\epsilon^2).
\]

Combine:

\[
y_\gamma
=
\frac{\epsilon}{3}+O(\epsilon^2).
\]

Thus weak measurement of the energy density at the Wilson-Fisher fixed point is relevant for

\[
\epsilon>0,
\]

that is, for

\[
d<4.
\]

## Why \(\Delta_\sigma=1/8\) and \(\Delta_\varepsilon=1\) in 2D Ising

The 2D Ising CFT has three primary fields:

\[
\mathbb{1},
\qquad
\sigma,
\qquad
\varepsilon.
\]

Their scaling dimensions are

\[
\Delta_{\mathbb{1}}=0,
\qquad
\Delta_\sigma=\frac18,
\qquad
\Delta_\varepsilon=1.
\]

Here is the simplest way to remember these numbers.

At a critical point, a two-point function decays as

\[
\langle \mathcal{O}(r)\mathcal{O}(0)\rangle
\sim
\frac{1}{r^{2\Delta_{\mathcal{O}}}}.
\]

For the 2D critical Ising spin field,

\[
\langle \sigma(r)\sigma(0)\rangle
\sim
r^{-1/4}.
\]

Compare this with

\[
\langle \sigma(r)\sigma(0)\rangle
\sim
r^{-2\Delta_\sigma}.
\]

So

\[
2\Delta_\sigma=\frac14.
\]

Divide by \(2\):

\[
\Delta_\sigma=\frac18.
\]

For the energy operator,

\[
\langle \varepsilon(r)\varepsilon(0)\rangle
\sim
r^{-2}.
\]

Compare this with

\[
\langle \varepsilon(r)\varepsilon(0)\rangle
\sim
r^{-2\Delta_\varepsilon}.
\]

So

\[
2\Delta_\varepsilon=2.
\]

Divide by \(2\):

\[
\Delta_\varepsilon=1.
\]

That is the most compact memory aid:

\[
\sigma\sigma\text{ correlator } \sim r^{-1/4}
\Rightarrow
\Delta_\sigma=\frac18.
\]

\[
\varepsilon\varepsilon\text{ correlator } \sim r^{-2}
\Rightarrow
\Delta_\varepsilon=1.
\]

## 2D Ising: measuring the spin

For spin measurement:

\[
\mathcal{O}=\sigma.
\]

The dimension is

\[
\Delta_{\mathcal{O}}=\Delta_\sigma=\frac18.
\]

The dimension is \(d=2\). Therefore

\[
y_\gamma=d-2\Delta_\sigma.
\]

Substitute:

\[
y_\gamma
=
2-2\left(\frac18\right).
\]

Multiply:

\[
2\left(\frac18\right)=\frac28=\frac14.
\]

So

\[
y_\gamma=2-\frac14.
\]

Write \(2=8/4\):

\[
y_\gamma=\frac84-\frac14.
\]

Therefore

\[
y_\gamma=\frac74.
\]

Since

\[
\frac74>0,
\]

spin measurement is strongly relevant.

## 2D Ising: measuring the energy

For energy measurement:

\[
\mathcal{O}=\varepsilon.
\]

The dimension is

\[
\Delta_{\mathcal{O}}=\Delta_\varepsilon=1.
\]

Again \(d=2\). Therefore

\[
y_\gamma=d-2\Delta_\varepsilon.
\]

Substitute:

\[
y_\gamma=2-2(1).
\]

Thus

\[
y_\gamma=2-2.
\]

So

\[
y_\gamma=0.
\]

Energy measurement is tree-level marginal. Tree-level power counting alone does not tell us whether it is marginally relevant or marginally irrelevant.

The perturbation is

\[
\delta S
=
-\gamma
\int d^2x
\sum_{a<b}
\varepsilon_a(x)\varepsilon_b(x).
\]

The single-copy fusion rule is

\[
\varepsilon\times\varepsilon=\mathbb{1}.
\]

This means

\[
C_{\varepsilon\varepsilon\varepsilon}=0.
\]

But this does not make the replicated beta function vanish. The reason is that two replica bilinears can share one replica index:

\[
\left[\varepsilon_a\varepsilon_b\right](x)
\left[\varepsilon_a\varepsilon_c\right](0)
\sim
\frac{1}{|x|^2}
\varepsilon_b(0)\varepsilon_c(0).
\]

This regenerates the same off-diagonal perturbation.

The standard beta function is

\[
\frac{d\gamma}{d\ell}
=
y_\gamma\gamma
+4\pi(R-2)\gamma^2
-16\pi^2(R-2)\gamma^3+\cdots.
\]

For 2D Ising energy measurement:

\[
y_\gamma=0.
\]

For measurement:

\[
R\to1.
\]

Substitute both:

\[
\frac{d\gamma}{d\ell}
=
0\cdot\gamma
+4\pi(1-2)\gamma^2
-16\pi^2(1-2)\gamma^3+\cdots.
\]

Now

\[
1-2=-1.
\]

Therefore

\[
\frac{d\gamma}{d\ell}
=
4\pi(-1)\gamma^2
-16\pi^2(-1)\gamma^3+\cdots.
\]

So

\[
\frac{d\gamma}{d\ell}
=
-4\pi\gamma^2
+16\pi^2\gamma^3+\cdots.
\]

At small positive \(\gamma\), the leading term is

\[
-4\pi\gamma^2<0.
\]

Therefore \(\gamma\) decreases under RG. Weak energy measurement in the 2D critical Ising model is marginally irrelevant.

## Final summary

For a weak measurement of an operator \(\mathcal{O}\):

\[
y_\gamma=d-2\Delta_{\mathcal{O}}.
\]

For a free scalar:

\[
\Delta_\phi=\frac{d-2}{2},
\qquad
y_\gamma=2.
\]

For Wilson-Fisher energy measurement in \(d=4-\epsilon\):

\[
\Delta_\varepsilon=2-\frac{2\epsilon}{3}+O(\epsilon^2),
\qquad
y_\gamma=\frac{\epsilon}{3}+O(\epsilon^2).
\]

For 2D Ising spin measurement:

\[
\Delta_\sigma=\frac18,
\qquad
y_\gamma=\frac74.
\]

For 2D Ising energy measurement:

\[
\Delta_\varepsilon=1,
\qquad
y_\gamma=0.
\]

The one-loop beta function then gives

\[
\frac{d\gamma}{d\ell}
=
-4\pi\gamma^2+16\pi^2\gamma^3+\cdots,
\]

so weak positive energy measurement is marginally irrelevant.

## References

- A. Nahum and K. J. Wiese, *Renormalization group for measurement and entanglement phase transitions*, arXiv:2303.07848.
- A. Nahum and J. Jacobsen, *Bayesian critical points in classical lattice models*, arXiv:2504.01264.
- K. J. Wiese, A. Das, and A. Nahum, *Bayesian phase transition for the critical Ising model: enlarged replica symmetry in the epsilon expansion and in 2D*, arXiv:2604.23346.
