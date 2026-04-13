# Crash Course: Hamiltonian Dynamics

## 1. State Space

For a system with generalized coordinates \(q_i\), \(i=1,\dots,n\), the classical state is
\[
(q_1,\dots,q_n,p_1,\dots,p_n),
\]
and the full state space is phase space
\[
\Gamma = T^*Q,
\]
which is \(2n\)-dimensional.

## 2. From Lagrangian to Hamiltonian

Start with \(L(q,\dot q,t)\) and define canonical momenta
\[
p_i = \frac{\partial L}{\partial \dot q_i}.
\]
If \(\dot q_i\) can be expressed in terms of \((q,p,t)\), define
\[
H(q,p,t)=\sum_i p_i\dot q_i - L.
\]

## 3. Canonical Symplectic Form

Canonical one-form:
\[
\theta = \sum_i p_i\,dq_i.
\]
Canonical symplectic form:
\[
\omega = -d\theta = \sum_i dq_i \wedge dp_i.
\]

Here \(\wedge\) is the *Keilprodukt* (wedge product):
- antisymmetric: \(dq_i \wedge dp_i = - dp_i \wedge dq_i\),
- alternating: \(dq_i \wedge dq_i = 0\),
- geometric meaning: oriented area element in phase space.

The symplectic form is closed (\(d\omega=0\)) and non-degenerate, and this is exactly the geometric structure behind Hamiltonian mechanics.

## 4. Hamilton's Equations

Dynamics is defined by
\[
\iota_{X_H}\omega = dH.
\]
In canonical coordinates this gives
\[
\dot q_i = \frac{\partial H}{\partial p_i}, \qquad
\dot p_i = -\frac{\partial H}{\partial q_i}.
\]

## 5. Poisson Brackets

For observables \(f(q,p,t)\), \(g(q,p,t)\):
\[
\{f,g\} =
\sum_i \left(
\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}
-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}
\right).
\]
Time evolution:
\[
\dot f = \{f,H\} + \frac{\partial f}{\partial t}.
\]
Canonical relations:
\[
\{q_i,q_j\}=0,\quad \{p_i,p_j\}=0,\quad \{q_i,p_j\}=\delta_{ij}.
\]

## 6. Constants of Motion and Symmetry

An observable \(f\) is conserved if
\[
\dot f=0.
\]
If \(f\) has no explicit time dependence, this is
\[
\{f,H\}=0.
\]
If \(H\) has no explicit time dependence, energy is conserved.

## 7. Canonical Transformations

A transformation \((q,p)\mapsto(Q,P)\) is canonical if it preserves \(\omega\) (equivalently Poisson brackets).  
Then Hamilton's equations keep their form.

## 8. Liouville Theorem

Hamiltonian flow preserves phase-space volume.  
This is why phase-space density is transported incompressibly along trajectories.

## 9. Example: 1D Harmonic Oscillator

\[
H=\frac{p^2}{2m}+\frac12 m\Omega^2 q^2.
\]
Hamilton equations:
\[
\dot q = \frac{p}{m}, \qquad
\dot p = -m\Omega^2 q.
\]
Therefore
\[
\ddot q+\Omega^2 q=0.
\]
In phase space, trajectories are ellipses of constant energy.

## 10. Minimal Workflow for Exercises

1. Choose coordinates \(q_i\), write \(L\).
2. Compute \(p_i=\partial L/\partial \dot q_i\).
3. Build \(H=\sum_i p_i\dot q_i-L\).
4. Write Hamilton equations.
5. Use Poisson brackets to identify conserved quantities.
