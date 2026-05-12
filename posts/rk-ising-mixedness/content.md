---
title: "Rokhsar-Kivelson States, Noisy Ising Measurements, and Mixedness"
date: 2026-05-12
excerpt: "A self-contained Ising note on RK states, diagonal noisy bond measurements, conditioned pure trajectories, and the exact mixed-state decoherence kernel."
tags: RK states, Ising model, measurements, mixed states, Nishimori line
---

This note explains the Ising Rokhsar-Kivelson construction from the ground up and isolates the precise place where **mixedness** enters. The point that often causes confusion is simple once written carefully:

- the RK state itself is pure,
- a noisy but efficient measurement gives a pure conditioned trajectory state,
- the state becomes mixed when we average over outcomes, or when part of the detector noise is hidden.

[Download the PDF](./rk_ising_mixedness_note.pdf)  
[Download the LaTeX source](./rk_ising_mixedness_note.tex)

## Overview

Rokhsar-Kivelson (RK) states are useful because they convert a classical Gibbs ensemble into a quantum wavefunction. In the Ising case this gives a very clean bridge between:

- classical thermal averages,
- quantum expectation values of diagonal operators,
- Bayesian conditioning under noisy bond measurements,
- replica and Nishimori-line arguments for higher moments.

The main goal here is to keep those four viewpoints separate and then connect them in a controlled way.

## Classical Ising Model

Take the classical Ising model on a square lattice with spins \( \sigma_i = \pm 1 \) and Hamiltonian

\[
H[\sigma] = - J \sum_{\langle ij\rangle} \sigma_i \sigma_j.
\]

The corresponding Gibbs ensemble at inverse temperature \( \beta \) is

\[
P_\beta(\sigma) = \frac{e^{-\beta H[\sigma]}}{Z(\beta)},
\qquad
Z(\beta)=\sum_{\{\sigma_i=\pm1\}} e^{-\beta H[\sigma]}.
\]

This is the classical probability distribution that the RK state will encode.

## RK Construction

The Ising RK state is

\[
\ket{\mathrm{RK}_\beta}
=
\frac{1}{\sqrt{Z(\beta)}}\sum_\sigma e^{-\beta H[\sigma]/2}\ket{\sigma}.
\]

The amplitude of a basis configuration is the square root of its Boltzmann weight, so

\[
\bigl|\langle \sigma \mid \mathrm{RK}_\beta \rangle \bigr|^2
=
\frac{e^{-\beta H[\sigma]}}{Z(\beta)}.
\]

This means the diagonal measurement probabilities of the quantum state reproduce the full classical Gibbs ensemble exactly.

## Diagonal Observables are Thermal Observables

Let \( \hat O \) be diagonal in the computational basis:

\[
\hat O \ket{\sigma}=O(\sigma)\ket{\sigma}.
\]

Then

\[
\langle \mathrm{RK}_\beta \vert \hat O \vert \mathrm{RK}_\beta \rangle
=
\frac{1}{Z(\beta)}\sum_\sigma O(\sigma)e^{-\beta H[\sigma]}.
\]

So every diagonal equal-time observable in the RK state is literally the corresponding thermal observable of the classical Ising model.

This is the first key bridge:

\[
\text{RK quantum expectation of diagonal observable}
\;=\;
\text{classical Gibbs expectation}.
\]

## Noisy Bond-Energy Measurements

Now measure the bond-energy operators

\[
\hat B_{ij}=\hat\sigma_i^z\hat\sigma_j^z,
\qquad
\hat B_{ij}\ket{\sigma}=(\sigma_i\sigma_j)\ket{\sigma}.
\]

For binary weak measurements with outcomes \(m_{ij}=\pm1\), use Kraus operators

\[
K_{\bm m}
=
\frac{1}{(2\cosh\tilde\gamma)^{N_b/2}}
\exp\!\left[
\frac{\tilde\gamma}{2}\sum_{\langle ij\rangle}m_{ij}\hat B_{ij}
\right].
\]

Here \(N_b\) is the number of bonds and \( \tilde\gamma \) is the measurement strength. Define

\[
\gamma=\tanh\tilde\gamma.
\]

Then the conditional probability of getting record \( \bm m \) given a definite classical configuration \( \sigma \) is

\[
P(\bm m \mid \sigma)
=
\prod_{\langle ij\rangle}
\frac{1+\gamma\,m_{ij}\sigma_i\sigma_j}{2}.
\]

This is a **noisy** measurement channel. The outcome is correlated with the bond variable \( \sigma_i\sigma_j \), but it does not reveal it perfectly unless \( \tilde\gamma\to\infty \).

## Conditioned State for a Fixed Measurement Record

If the observed measurement record is \( \bm m \), the conditioned post-measurement state is

\[
\ket{\Psi_{\bm m}}
=
\frac{K_{\bm m}\ket{\mathrm{RK}_\beta}}{\sqrt{p(\bm m)}},
\qquad
p(\bm m)=
\langle \mathrm{RK}_\beta \vert K_{\bm m}^\dagger K_{\bm m}\vert \mathrm{RK}_\beta \rangle.
\]

Since the measurement is diagonal, this becomes

\[
\ket{\Psi_{\bm m}}
\propto
\sum_\sigma
\exp\!\left[
-\frac{\beta}{2}H[\sigma]
+\frac{\tilde\gamma}{2}\sum_{\langle ij\rangle}m_{ij}\sigma_i\sigma_j
\right]\ket{\sigma}.
\]

This is still a **pure state**.

That is the central conceptual point:

> Noisy measurement does not by itself imply a mixed conditioned state.

If the full outcome record is known and the measurement is efficient, each trajectory state remains pure.

## Bayesian Interpretation

The same formula has a direct classical meaning. The posterior probability of configuration \( \sigma \) given the observed record \( \bm m \) is

\[
P(\sigma \mid \bm m)
=
\frac{
e^{-\beta H[\sigma]+\tilde\gamma\sum_{\langle ij\rangle}m_{ij}\sigma_i\sigma_j}
}{
Z[\bm m]
},
\]

with

\[
Z[\bm m]
=
\sum_\sigma
e^{-\beta H[\sigma]+\tilde\gamma\sum_{\langle ij\rangle}m_{ij}\sigma_i\sigma_j}.
\]

So the same object can be read in two ways:

- as a conditioned pure quantum trajectory state,
- or as a classical Bayesian posterior distribution.

This is the second key bridge:

\[
\text{conditioned RK trajectory}
\; \leftrightarrow \;
\text{Bayesian posterior}.
\]

## Where Mixedness Actually Enters

The state becomes mixed when we discard the record and average over outcomes:

\[
\bar\rho
=
\sum_{\bm m} p(\bm m)\ket{\Psi_{\bm m}}\bra{\Psi_{\bm m}}
=
\sum_{\bm m} K_{\bm m}\ket{\mathrm{RK}_\beta}\bra{\mathrm{RK}_\beta}K_{\bm m}^\dagger.
\]

That is the **unconditioned** or **outcome-averaged** state, and it is generally mixed.

So the correct logic is:

- full record kept \( \Rightarrow \) conditioned trajectory,
- outcomes averaged out \( \Rightarrow \) mixed state.

## Exact Decoherence Kernel

For this binary Ising channel one can compute the outcome-averaged state exactly in the computational basis. Write

\[
\psi_\beta(\sigma)=\frac{e^{-\beta H[\sigma]/2}}{\sqrt{Z(\beta)}}.
\]

Then

\[
\bar\rho_{\sigma,\sigma'}
=
\psi_\beta(\sigma)\psi_\beta(\sigma')\,
\Gamma_{\tilde\gamma}(\sigma,\sigma'),
\]

where

\[
\Gamma_{\tilde\gamma}(\sigma,\sigma')
=
\bigl(\sech\tilde\gamma\bigr)^{d_B(\sigma,\sigma')}.
\]

Here \(d_B(\sigma,\sigma')\) is the number of bonds on which the two configurations have different bond energies:

\[
d_B(\sigma,\sigma')
:=
\#\bigl\{\langle ij\rangle : \sigma_i\sigma_j \neq \sigma_i'\sigma_j' \bigr\}.
\]

This formula says everything at once:

- diagonal entries are unchanged,
- off-diagonal coherence is suppressed,
- the suppression is stronger when the two configurations disagree on more measured bonds,
- the suppression becomes stronger as \( \tilde\gamma \) increases.

This is the precise mixed-state structure of the monitored RK state after averaging over outcomes.

## Why the First Measurement-Averaged Moment is Clean

Let \( \hat O \) again be diagonal in the Ising basis. Then

\[
\sum_{\bm m} p(\bm m)\,\langle \hat O\rangle_{\bm m}
=
\mathrm{Tr}(\hat O\,\bar\rho).
\]

But the decohering channel changes only the off-diagonal matrix elements. Since \( \hat O \) is diagonal, it sees only the diagonal of \( \bar\rho \), which is the same as the diagonal of the original RK density matrix. Therefore

\[
\sum_{\bm m} p(\bm m)\,\langle \hat O\rangle_{\bm m}
=
\langle \mathrm{RK}_\beta \vert \hat O \vert \mathrm{RK}_\beta \rangle.
\]

Equivalently, in the Bayesian language,

\[
\sum_{\bm m} P(\bm m)\,\langle O\rangle_{\bm m}
=
\frac{1}{Z(\beta)}\sum_\sigma O(\sigma)e^{-\beta H[\sigma]}.
\]

So the first measurement-averaged moment is exactly equal to the unmeasured thermal expectation value.

This is a statement about **diagonal observables after averaging over outcomes**. It is not a statement that the monitored state remains pure, and it is not by itself a statement that the full monitored problem is critical.

## What the Higher Nishimori Line Adds

The first-moment identity above does **not** require any Nishimori condition. It follows from POVM completeness and diagonality.

The higher Nishimori line enters when one studies **higher moments** using replicas. For Gaussian bond measurements, the replicated theory takes the form

\[
-\mathcal H_{\mathrm{rep}}
=
\beta\sum_{a=1}^R\sum_{\langle ij\rangle}\sigma_i^{(a)}\sigma_j^{(a)}
+\frac{\Delta}{2}
\sum_{\substack{a,b=1\\a\neq b}}^R
\sum_{\langle ij\rangle}
\sigma_i^{(a)}\sigma_j^{(a)}\sigma_i^{(b)}\sigma_j^{(b)}.
\]

On the line

\[
\beta=\Delta,
\]

this theory reorganizes into a gauge-invariant form with one extra replica and enlarged replica symmetry. In the Gaussian Ising case this leads to a much stronger statement than the first-moment identity:

\[
\bigl[\langle \sigma_i\sigma_j\rangle_{\bm m}^2\bigr]_{\bm m}
=
\bigl[\langle \sigma_i\sigma_j\rangle_{\bm m}\bigr]_{\bm m}
=
\langle \sigma_i\sigma_j\rangle_{\mathrm{clean}}.
\]

That is the higher-Nishimori mechanism behind the exact equality between the Edwards-Anderson exponent and the clean Ising spin-correlation exponent.

## Efficient versus Inefficient Measurements

There is one more distinction that matters.

If the measurement is **efficient**, the full microscopic record is known, and each conditioned trajectory is pure.

If the measurement is **inefficient**, some detector noise is hidden. Then one observed outcome may correspond to several unresolved microscopic outcomes, and even the conditioned state can already be mixed:

\[
\rho_m
=
\frac{\sum_\mu K_{m,\mu}\rho_0 K_{m,\mu}^\dagger}
{\mathrm{Tr}\!\left(\sum_\mu K_{m,\mu}\rho_0 K_{m,\mu}^\dagger\right)}.
\]

So there are really two routes to mixedness:

- averaging over observed outcomes,
- or losing part of the measurement record itself.

## Takeaway

For the Ising RK state the conceptual structure is:

1. The RK state is a pure square-root Gibbs state.
2. Diagonal observables in the RK state reproduce classical thermal observables.
3. Noisy diagonal bond measurements define a Bayesian posterior for each record.
4. The conditioned trajectory state is pure if the measurement is efficient.
5. The outcome-averaged state is mixed, with exact decoherence kernel
   \[
   \bar\rho_{\sigma,\sigma'}
   \propto
   e^{-\beta(H[\sigma]+H[\sigma'])/2}
   (\sech\tilde\gamma)^{d_B(\sigma,\sigma')}.
   \]
6. The first measurement-averaged moment of any diagonal observable is exactly equal to its unmeasured value.
7. Extra higher-Nishimori structure appears only when one studies higher moments with replicas.

## References

1. D. S. Rokhsar and S. A. Kivelson, “Superconductivity and the Quantum Hard-Core Dimer Gas,” *Phys. Rev. Lett.* **61**, 2376 (1988).
2. Y. Iba, “The Nishimori line and Bayesian Statistics,” *J. Phys. A* **32**, 3875 (1999).
3. A. Nahum and J. L. Jacobsen, “Bayesian critical points in classical lattice models,” arXiv:2504.01264.
4. R. A. Patil, M. Pütz, S. Trebst, G.-Y. Zhu, and A. W. W. Ludwig, “Higher Nishimori Criticality and Exact Results at the Learning Transition of Deformed Toric Codes,” arXiv:2604.06324.
