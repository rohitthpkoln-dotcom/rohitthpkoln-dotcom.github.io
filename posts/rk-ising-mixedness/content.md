---
title: "Rokhsar-Kivelson States, Noisy Ising Measurements, and Mixedness"
date: 2026-05-12
excerpt: "A detailed Ising note deriving the RK wavefunction, the Bayesian posterior under noisy bond measurements, the exact outcome-averaged mixed state, and the first-moment identity."
tags: RK states, Ising model, measurements, mixed states, Nishimori line
---

## Introduction

This note explains the Ising Rokhsar-Kivelson construction carefully enough that one can see exactly where pure states end, where mixed states begin, and why noisy measurement does not by itself imply mixedness. The clean way to organize the discussion is to keep three different objects separate from the start.

The first object is the unmeasured Rokhsar-Kivelson state itself. This is a pure quantum state. The second object is the post-measurement state conditioned on a particular observed measurement record. For an efficient measurement, this is also a pure state, even though the measurement is weak and noisy. The third object is the state obtained after averaging over all outcomes. That state is generally mixed, and in the Ising bond-measurement problem its matrix elements can be computed exactly.

The same formalism also has a classical Bayesian interpretation. The squared amplitudes of the RK wavefunction give a Gibbs prior, the measurement channel gives a likelihood, and the conditioned post-measurement state has diagonal probabilities equal to the corresponding posterior distribution. This is the precise sense in which the monitored Ising RK problem and the Bayesian inference problem are the same problem written in two different languages.

## The Classical Ising Model

Consider the classical Ising model on a square lattice with spins \( \sigma_i = \pm 1 \) and Hamiltonian

\[
H[\sigma] = - J \sum_{\langle ij\rangle} \sigma_i \sigma_j .
\]

The Gibbs ensemble at inverse temperature \( \beta \) is

\[
P_\beta(\sigma) = \frac{e^{-\beta H[\sigma]}}{Z(\beta)},
\qquad
Z(\beta) = \sum_{\{\sigma_i = \pm 1\}} e^{-\beta H[\sigma]} .
\]

It is useful to emphasize that \( \sigma \) denotes an entire spin configuration, not a single spin. Thus \( H[\sigma] \) is the classical energy of a configuration and \( P_\beta(\sigma) \) is the classical thermal probability of that configuration.

## The Rokhsar-Kivelson State

The corresponding Rokhsar-Kivelson state is

\[
|\mathrm{RK}_\beta\rangle
=
\frac{1}{\sqrt{Z(\beta)}}
\sum_\sigma e^{-\beta H[\sigma]/2} |\sigma\rangle .
\]

This is a pure quantum state in the computational basis \( |\sigma\rangle \). Its amplitude for a configuration \( \sigma \) is the square root of the classical Boltzmann weight. Squaring the amplitude gives

\[
|\langle \sigma | \mathrm{RK}_\beta \rangle|^2
=
\frac{e^{-\beta H[\sigma]}}{Z(\beta)}
=
P_\beta(\sigma) .
\]

So the diagonal probability distribution of the RK state is exactly the classical Ising Gibbs ensemble. This is the basic RK correspondence.

Now let \( \hat O \) be any operator diagonal in the computational basis,

\[
\hat O |\sigma\rangle = O(\sigma) |\sigma\rangle .
\]

Then

\[
\langle \mathrm{RK}_\beta | \hat O | \mathrm{RK}_\beta \rangle
=
\frac{1}{Z(\beta)}
\sum_\sigma O(\sigma) e^{-\beta H[\sigma]} .
\]

Thus every diagonal equal-time quantum expectation value in the RK state is exactly the corresponding thermal expectation value of the classical Ising model. In particular, if \( O(\sigma) = \sigma_i \sigma_j \), then the quantum expectation value of the diagonal operator \( \hat \sigma_i^z \hat \sigma_j^z \) is exactly the ordinary Ising two-point correlator at inverse temperature \( \beta \).

## Noisy Bond Measurements

We now measure the bond-energy operators

\[
\hat B_{ij} = \hat \sigma_i^z \hat \sigma_j^z ,
\qquad
\hat B_{ij} |\sigma\rangle = (\sigma_i \sigma_j) |\sigma\rangle .
\]

For each bond \( \langle ij\rangle \), the corresponding classical quantity is \( \sigma_i \sigma_j = \pm 1 \). A convenient model of a noisy binary weak measurement uses outcomes \( m_{ij} = \pm 1 \) and Kraus operators

\[
K_{\mathbf m}
=
\frac{1}{(2\cosh \tilde\gamma)^{N_b/2}}
\exp\!\left[
\frac{\tilde\gamma}{2}
\sum_{\langle ij\rangle} m_{ij} \hat B_{ij}
\right] ,
\]

where \( \mathbf m = \{m_{ij}\} \), \( N_b \) is the total number of bonds, and \( \tilde\gamma \ge 0 \) controls the measurement strength.

Because all \( \hat B_{ij} \) are diagonal in the \( |\sigma\rangle \) basis, the Kraus operator is diagonal as well. Acting on a basis state gives

\[
K_{\mathbf m} |\sigma\rangle
=
\frac{1}{(2\cosh \tilde\gamma)^{N_b/2}}
\exp\!\left[
\frac{\tilde\gamma}{2}
\sum_{\langle ij\rangle} m_{ij} \sigma_i \sigma_j
\right]
|\sigma\rangle .
\]

The corresponding conditional probability of obtaining the record \( \mathbf m \) if the system were known to be in the definite configuration \( \sigma \) is

\[
P(\mathbf m \mid \sigma)
=
\langle \sigma | K_{\mathbf m}^\dagger K_{\mathbf m} | \sigma \rangle .
\]

Using the diagonality of \( K_{\mathbf m} \), this becomes

\[
P(\mathbf m \mid \sigma)
=
\frac{1}{(2\cosh \tilde\gamma)^{N_b}}
\exp\!\left[
\tilde\gamma
\sum_{\langle ij\rangle} m_{ij} \sigma_i \sigma_j
\right] .
\]

Because the exponent is a sum over bonds, this factorizes:

\[
P(\mathbf m \mid \sigma)
=
\prod_{\langle ij\rangle}
\frac{e^{\tilde\gamma m_{ij}\sigma_i\sigma_j}}{2\cosh \tilde\gamma} .
\]

If we define

\[
\gamma = \tanh \tilde\gamma ,
\]

then for a single bond one has

\[
\frac{e^{\tilde\gamma m \sigma}}{2\cosh \tilde\gamma}
=
\frac{1 + \gamma\, m \sigma}{2},
\qquad
m = \pm 1,\ \sigma = \pm 1 .
\]

Therefore the full likelihood can be written as

\[
P(\mathbf m \mid \sigma)
=
\prod_{\langle ij\rangle}
\frac{1 + \gamma\, m_{ij}\sigma_i\sigma_j}{2} .
\]

This formula makes the meaning of the channel transparent. If \( \tilde\gamma = 0 \), then \( \gamma = 0 \) and the outcomes are completely random. If \( \tilde\gamma \to \infty \), then \( \gamma \to 1 \) and the outcome approaches the exact bond value. For finite \( \tilde\gamma \), the outcome is noisy but correlated with the bond energy.

## The Conditioned Post-Measurement State

Suppose the initial state is the pure RK state \( |\mathrm{RK}_\beta\rangle \), and suppose the observed measurement record is \( \mathbf m \). The conditioned post-measurement state is

\[
|\Psi_{\mathbf m}\rangle
=
\frac{K_{\mathbf m} |\mathrm{RK}_\beta\rangle}{\sqrt{p(\mathbf m)}} ,
\]

where

\[
p(\mathbf m)
=
\langle \mathrm{RK}_\beta | K_{\mathbf m}^\dagger K_{\mathbf m} | \mathrm{RK}_\beta \rangle
\]

is the probability of that record.

Substituting the RK wavefunction gives

\[
|\Psi_{\mathbf m}\rangle
\propto
\sum_\sigma
e^{-\beta H[\sigma]/2}
\exp\!\left[
\frac{\tilde\gamma}{2}
\sum_{\langle ij\rangle} m_{ij}\sigma_i\sigma_j
\right]
|\sigma\rangle .
\]

Combining the exponents,

\[
|\Psi_{\mathbf m}\rangle
\propto
\sum_\sigma
\exp\!\left[
-\frac{\beta}{2} H[\sigma]
+ \frac{\tilde\gamma}{2}
\sum_{\langle ij\rangle} m_{ij}\sigma_i\sigma_j
\right]
|\sigma\rangle .
\]

This is a pure state. The measurement is weak, stochastic, and noisy, but once the complete record \( \mathbf m \) is known, the conditioned state is still pure. The noise in the measurement does not by itself produce mixedness.

This is the first point that often gets blurred in informal discussion: weak noisy measurement and mixedness are not the same thing. Mixedness appears only when information is discarded or hidden.

## Classical Bayesian Interpretation

The same conditioned object has a classical interpretation. The RK state provides the prior

\[
P_\beta(\sigma) = \frac{e^{-\beta H[\sigma]}}{Z(\beta)},
\]

and the noisy measurement channel provides the likelihood \( P(\mathbf m \mid \sigma) \). Therefore Bayes' theorem gives

\[
P(\sigma \mid \mathbf m)
=
\frac{P(\mathbf m \mid \sigma) P_\beta(\sigma)}{P(\mathbf m)} .
\]

Using the exponential form of the likelihood,

\[
P(\sigma \mid \mathbf m)
\propto
e^{-\beta H[\sigma]}
\exp\!\left[
\tilde\gamma
\sum_{\langle ij\rangle} m_{ij}\sigma_i\sigma_j
\right] ,
\]

so after dropping the normalization-independent constant one finds

\[
P(\sigma \mid \mathbf m)
=
\frac{
\exp\!\left[
-\beta H[\sigma]
+ \tilde\gamma
\sum_{\langle ij\rangle} m_{ij}\sigma_i\sigma_j
\right]
}{
Z[\mathbf m]
},
\]

with

\[
Z[\mathbf m]
=
\sum_\sigma
\exp\!\left[
-\beta H[\sigma]
+ \tilde\gamma
\sum_{\langle ij\rangle} m_{ij}\sigma_i\sigma_j
\right] .
\]

Thus the conditioned measurement problem is exactly a Bayesian inference problem for an Ising model with the same thermal prior and a noisy bond-observation channel.

Moreover, the diagonal probabilities of the conditioned quantum state \( |\Psi_{\mathbf m}\rangle \) are exactly this posterior distribution. So the conditioned pure quantum trajectory and the classical posterior are two descriptions of the same conditioned object.

## The Outcome-Averaged State and Mixedness

Now consider what happens if the measurement record is not retained. The resulting state is the outcome-averaged density matrix

\[
\bar\rho
=
\sum_{\mathbf m} p(\mathbf m)\,
|\Psi_{\mathbf m}\rangle \langle \Psi_{\mathbf m}|
=
\sum_{\mathbf m}
K_{\mathbf m}
|\mathrm{RK}_\beta\rangle \langle \mathrm{RK}_\beta|
K_{\mathbf m}^\dagger .
\]

This state is generally mixed. The cleanest way to see why is to compute its matrix elements in the computational basis.

Write

\[
\psi_\beta(\sigma)
=
\frac{e^{-\beta H[\sigma]/2}}{\sqrt{Z(\beta)}} .
\]

Then

\[
|\mathrm{RK}_\beta\rangle
=
\sum_\sigma \psi_\beta(\sigma) |\sigma\rangle ,
\]

and therefore

\[
\bar\rho_{\sigma,\sigma'}
=
\langle \sigma | \bar\rho | \sigma' \rangle
=
\psi_\beta(\sigma)\psi_\beta(\sigma')
\sum_{\mathbf m}
\langle \sigma | K_{\mathbf m} | \sigma \rangle
\langle \sigma' | K_{\mathbf m} | \sigma' \rangle .
\]

Using the explicit diagonal matrix elements of the Kraus operators,

\[
\langle \sigma | K_{\mathbf m} | \sigma \rangle
=
\frac{1}{(2\cosh \tilde\gamma)^{N_b/2}}
\exp\!\left[
\frac{\tilde\gamma}{2}
\sum_{\langle ij\rangle} m_{ij}\sigma_i\sigma_j
\right] ,
\]

and similarly for \( \sigma' \). Multiplying them gives

\[
\bar\rho_{\sigma,\sigma'}
=
\psi_\beta(\sigma)\psi_\beta(\sigma')
\prod_{\langle ij\rangle}
\left[
\frac{1}{2\cosh \tilde\gamma}
\sum_{m_{ij}=\pm 1}
\exp\!\left(
\frac{\tilde\gamma}{2}
m_{ij}\sigma_i\sigma_j
\right)
\exp\!\left(
\frac{\tilde\gamma}{2}
m_{ij}\sigma_i'\sigma_j'
\right)
\right] .
\]

Combining the bond contributions more cleanly,

\[
\bar\rho_{\sigma,\sigma'}
=
\psi_\beta(\sigma)\psi_\beta(\sigma')
\prod_{\langle ij\rangle}
\frac{1}{2\cosh \tilde\gamma}
\sum_{m_{ij}=\pm 1}
\exp\!\left[
\frac{\tilde\gamma}{2}
m_{ij}\bigl(\sigma_i\sigma_j+\sigma_i'\sigma_j'\bigr)
\right] .
\]

The sum over \( m_{ij}=\pm 1 \) is elementary:

\[
\sum_{m=\pm 1}
\exp\!\left[
\frac{\tilde\gamma}{2}
m(A+B)
\right]
=
2 \cosh\!\left[
\frac{\tilde\gamma}{2}(A+B)
\right] ,
\]

with \( A = \sigma_i\sigma_j \) and \( B = \sigma_i'\sigma_j' \). Thus

\[
\bar\rho_{\sigma,\sigma'}
=
\psi_\beta(\sigma)\psi_\beta(\sigma')
\prod_{\langle ij\rangle}
\frac{
\cosh\!\left[
\frac{\tilde\gamma}{2}
\bigl(\sigma_i\sigma_j+\sigma_i'\sigma_j'\bigr)
\right]
}{
\cosh \tilde\gamma
} .
\]

Since \( \sigma_i\sigma_j \) and \( \sigma_i'\sigma_j' \) are each \( \pm 1 \), there are only two cases on each bond.

If the two configurations agree on that bond, then

\[
\sigma_i\sigma_j = \sigma_i'\sigma_j' ,
\]

so the sum in the argument of the hyperbolic cosine is \( \pm 2 \), and one gets

\[
\frac{\cosh(\tilde\gamma)}{\cosh(\tilde\gamma)} = 1 .
\]

If they disagree on that bond, then

\[
\sigma_i\sigma_j = - \sigma_i'\sigma_j' ,
\]

so the sum is zero and one gets

\[
\frac{\cosh(0)}{\cosh(\tilde\gamma)}
=
\frac{1}{\cosh(\tilde\gamma)} .
\]

Therefore each bond contributes either \( 1 \) or \( (\cosh \tilde\gamma)^{-1} \), depending on whether the two configurations agree or disagree on that bond energy. Define the bond-disagreement number

\[
d_B(\sigma,\sigma')
=
\sum_{\langle ij\rangle}
\frac{1 - \sigma_i\sigma_j \sigma_i'\sigma_j'}{2} .
\]

Then the exact outcome-averaged density matrix is

\[
\bar\rho_{\sigma,\sigma'}
=
\frac{e^{-\beta(H[\sigma]+H[\sigma'])/2}}{Z(\beta)}
\left( \frac{1}{\cosh \tilde\gamma} \right)^{d_B(\sigma,\sigma')} .
\]

This is the exact decoherence kernel of the monitored Ising RK state.

Several important facts are immediate. First, the diagonal elements are unchanged, because \( d_B(\sigma,\sigma)=0 \). Second, the off-diagonal elements are suppressed whenever the two configurations differ on measured bond energies. Third, stronger measurement means stronger decoherence, because \( (\cosh \tilde\gamma)^{-1} < 1 \) for \( \tilde\gamma > 0 \).

This formula gives the precise meaning of mixedness in this problem. The unconditioned state keeps the same diagonal Gibbs weights but loses off-diagonal coherence in a bond-by-bond way controlled by the measurement strength.

## Why the First Measurement-Averaged Moment is Unchanged

Now let \( O(\sigma) \) be any diagonal observable. For a fixed measurement record \( \mathbf m \), its conditioned expectation value is

\[
\langle O \rangle_{\mathbf m}
=
\sum_\sigma O(\sigma) P(\sigma \mid \mathbf m) .
\]

Average this over outcomes:

\[
\sum_{\mathbf m} P(\mathbf m)\, \langle O \rangle_{\mathbf m}
=
\sum_{\mathbf m} P(\mathbf m)
\sum_\sigma O(\sigma) P(\sigma \mid \mathbf m) .
\]

Using Bayes' theorem,

\[
P(\mathbf m) P(\sigma \mid \mathbf m)
=
P(\mathbf m \mid \sigma) P_\beta(\sigma) ,
\]

so

\[
\sum_{\mathbf m} P(\mathbf m)\, \langle O \rangle_{\mathbf m}
=
\sum_\sigma O(\sigma) P_\beta(\sigma)
\sum_{\mathbf m} P(\mathbf m \mid \sigma) .
\]

But for each fixed \( \sigma \), the conditional probabilities sum to one:

\[
\sum_{\mathbf m} P(\mathbf m \mid \sigma) = 1 .
\]

Therefore

\[
\sum_{\mathbf m} P(\mathbf m)\, \langle O \rangle_{\mathbf m}
=
\sum_\sigma O(\sigma) P_\beta(\sigma)
=
\frac{1}{Z(\beta)}
\sum_\sigma O(\sigma)e^{-\beta H[\sigma]} .
\]

This is exactly the unmeasured thermal expectation value.

In quantum language, the same identity says that for any operator diagonal in the computational basis,

\[
\sum_{\mathbf m} p(\mathbf m)\,
\langle \Psi_{\mathbf m} | \hat O | \Psi_{\mathbf m} \rangle
=
\langle \mathrm{RK}_\beta | \hat O | \mathrm{RK}_\beta \rangle .
\]

The reason is that the measurement channel changes only off-diagonal coherence. A diagonal observable depends only on the diagonal entries of the density matrix, and those remain equal to the classical Gibbs probabilities after outcome averaging.

This identity is extremely important, but it should not be over-interpreted. It does not say that the monitored state remains pure. It does not say that all moments are equal to the clean ones. It says only that the first outcome-averaged moment of a diagonal observable equals its unmeasured thermal expectation value.

## Relation to the Higher Nishimori Line

The first-moment identity just derived does not require any Nishimori condition. It follows directly from completeness of the measurement channel and diagonality of the measured operators.

The higher Nishimori structure enters only when one studies higher moments, especially the second moment, by replicas. For Gaussian bond measurements one obtains a replicated theory of the form

\[
-\mathcal H_{\mathrm{rep}}
=
\beta \sum_{a=1}^R \sum_{\langle ij\rangle} \sigma_i^{(a)}\sigma_j^{(a)}
+
\frac{\Delta}{2}
\sum_{\substack{a,b=1 \\ a\neq b}}^R
\sum_{\langle ij\rangle}
\sigma_i^{(a)}\sigma_j^{(a)}\sigma_i^{(b)}\sigma_j^{(b)} .
\]

On the line

\[
\beta = \Delta ,
\]

this theory acquires an enlarged gauge-invariant formulation with one extra replica. In the Gaussian Ising case, that higher-Nishimori structure implies a much stronger identity than the first-moment statement:

\[
\bigl[\langle \sigma_i\sigma_j\rangle_{\mathbf m}^2\bigr]_{\mathbf m}
=
\bigl[\langle \sigma_i\sigma_j\rangle_{\mathbf m}\bigr]_{\mathbf m}
=
\langle \sigma_i\sigma_j\rangle_{\mathrm{clean}} .
\]

This is why, at the higher Nishimori critical point, the Edwards-Anderson correlator has the same power-law exponent as the ordinary clean Ising spin-spin correlator.

## Efficient and Inefficient Measurements

There is one further distinction that matters for mixedness. Everything above assumed that the complete measurement record is known. That is what is meant by an efficient measurement. In that case the conditioned state for a given record is pure.

If some detector noise is hidden, then one may observe only a coarse-grained outcome \( m \), while a finer microscopic outcome \( \mu \) remains unresolved. In that case the conditioned state for the coarse outcome is

\[
\rho_m
=
\frac{
\sum_\mu K_{m,\mu}\rho_0 K_{m,\mu}^\dagger
}{
\mathrm{Tr}\!\left(
\sum_\mu K_{m,\mu}\rho_0 K_{m,\mu}^\dagger
\right)
} .
\]

This state can already be mixed even before one averages over the visible outcomes \( m \). So there are two distinct mechanisms for mixedness. One is averaging over observed measurement outcomes. The other is ignorance of part of the microscopic measurement record.

## Conclusion

The Ising RK construction gives a very clean example in which all the conceptual layers can be written down explicitly. The unmeasured RK state is a pure square-root Gibbs state. A noisy bond measurement with a known full outcome record produces a conditioned pure trajectory state whose diagonal probabilities are the Bayesian posterior. The outcome-averaged state is mixed, and its exact matrix elements can be computed in closed form:

\[
\bar\rho_{\sigma,\sigma'}
=
\frac{e^{-\beta(H[\sigma]+H[\sigma'])/2}}{Z(\beta)}
\left( \frac{1}{\cosh \tilde\gamma} \right)^{d_B(\sigma,\sigma')} .
\]

This formula makes the structure of the monitored state completely explicit. The diagonal classical probabilities are untouched, while the off-diagonal quantum coherence is damped according to the number of measured bonds on which two configurations disagree. The first measurement-averaged moment of any diagonal observable remains equal to its unmeasured thermal expectation value, but higher moments require replica methods and, in special cases, Nishimori-type identities.

## References

1. D. S. Rokhsar and S. A. Kivelson, “Superconductivity and the Quantum Hard-Core Dimer Gas,” *Physical Review Letters* **61**, 2376 (1988).
2. Y. Iba, “The Nishimori line and Bayesian Statistics,” *Journal of Physics A* **32**, 3875 (1999).
3. A. Nahum and J. L. Jacobsen, “Bayesian critical points in classical lattice models,” arXiv:2504.01264.
4. R. A. Patil, M. Pütz, S. Trebst, G.-Y. Zhu, and A. W. W. Ludwig, “Higher Nishimori Criticality and Exact Results at the Learning Transition of Deformed Toric Codes,” arXiv:2604.06324.
