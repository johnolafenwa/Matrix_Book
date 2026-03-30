# Chapter 11: Diagonalization and Dynamics

The previous chapter introduced eigenvalues and eigenvectors. Now we push that idea further.

If a matrix has enough independent eigenvectors, we can use them as a basis. In that basis, the matrix becomes diagonal. That is a huge simplification. Diagonal matrices are easy to understand, easy to raise to powers, and easy to use in modeling repeated processes.

This chapter is about that simplification and what it means for dynamics.

## Why diagonal form matters

A diagonal matrix acts independently on each coordinate:

```text
[d1 0  0 ] [x1]   [d1 x1]
[0  d2 0 ] [x2] = [d2 x2]
[0  0  d3] [x3]   [d3 x3]
```

No coordinate mixing happens.

That means:

- powers are easy: `D^k` just raises diagonal entries to the `k`th power
- long-term behavior is visible immediately
- complicated dynamics become coordinate-wise scaling

So diagonalization is really a change-of-coordinates trick that makes a matrix reveal its structure.

## The central idea

Suppose `A` has `n` linearly independent eigenvectors `v_1, ..., v_n` with eigenvalues `lambda_1, ..., lambda_n`.

Build the matrix

`P = [v_1 v_2 ... v_n]`

using those eigenvectors as columns, and let

`D = diag(lambda_1, ..., lambda_n)`

Then

`AP = PD`

and therefore

`A = P D P^-1`

This is diagonalization.

It says:

- `P^-1` changes ordinary coordinates into eigenvector coordinates
- `D` scales each eigenvector coordinate separately
- `P` changes back to the original coordinates

## A machine analogy

Think of a complicated machine with gears linked in awkward ways. In the original view, everything seems coupled.

Diagonalization is like opening the machine and discovering a hidden coordinate system in which each gear spins independently.

The system was always doing something simple. We just were not looking from the right angle.

## A visual flow

```mermaid
flowchart LR
    X["Original coordinates"] --> PINV["Change basis with P^-1"]
    PINV --> E["Eigenvector coordinates"]
    E --> D["Scale by D"]
    D --> P["Change back with P"]
    P --> Y["Result in original coordinates"]
```

## A worked example

Let

```text
A = [4 1]
    [2 3]
```

From Chapter 10, the eigenvalues are `5` and `2`, with eigenvectors

```text
v1 = [ 1]
     [ 1]

v2 = [ 1]
     [-2]
```

So

```text
P = [1  1 ]
    [1 -2]

D = [5 0]
    [0 2]
```

Because the eigenvectors are independent, `P` is invertible and

`A = P D P^-1`

This means that to understand powers of `A`, we can work with `D`.

## Powers become easy

If

`A = P D P^-1`

then

`A^k = P D^k P^-1`

because the middle terms collapse:

`(PDP^-1)(PDP^-1) = PD^2P^-1`

and so on.

Since `D` is diagonal,

`D^k = diag(lambda_1^k, ..., lambda_n^k)`

This is one of the main reasons diagonalization is useful.

## Repeated action as dynamics

Many systems evolve in discrete time:

`x_{k+1} = A x_k`

Examples:

- a population model updated each year
- a financial state updated each month
- probabilities moving through a network
- repeated transformations in computer graphics

Then

`x_k = A^k x_0`

So understanding the system means understanding powers of `A`.

Diagonalization turns that into a problem about powers of eigenvalues.

<figure class="book-media">
  <video controls playsinline preload="metadata" src="/media/animations/ch11-diagonal-dynamics.mp4"></video>
  <figcaption>Repeated multiplication bends the state toward the dominant eigendirection. This is the dynamic picture diagonalization helps explain.</figcaption>
</figure>

## Decomposing the initial state

Suppose

`x_0 = c_1 v_1 + c_2 v_2 + ... + c_n v_n`

Then

`A^k x_0 = c_1 lambda_1^k v_1 + c_2 lambda_2^k v_2 + ... + c_n lambda_n^k v_n`

This formula is fundamental.

It says each eigenvector component evolves independently, multiplied by its eigenvalue power.

So the long-term behavior of the whole system is governed by the largest eigenvalue magnitudes.

## Example: a simple growth system

Consider

```text
D = [1.2 0]
    [0 0.8]
```

If the initial vector is

`x_0 = [5, 7]^T`

then after `k` steps

`x_k = [1.2^k · 5, 0.8^k · 7]^T`

The first coordinate grows. The second decays.

As `k` becomes large, the first coordinate dominates.

## Stability from eigenvalues

For systems `x_{k+1} = A x_k`, eigenvalues provide a quick stability guide.

In a diagonalizable system:

- if all eigenvalues satisfy `|lambda| < 1`, solutions tend to `0`
- if any eigenvalue has `|lambda| > 1`, some directions grow
- if `|lambda| = 1`, behavior may persist or oscillate
- if `lambda < 0`, signs can alternate

This gives a high-level view of the dynamics before doing detailed calculations.

## A population-style example

Suppose two age groups evolve according to

```text
A = [0.9 0.4]
    [0.1 0.8]
```

Each step updates the population by mixing survival and movement between groups.

You could simulate this by repeated multiplication, but diagonalization gives more insight:

- which combination of groups grows or shrinks
- whether there is a dominant pattern
- which directions decay fastest

Even when you do not compute the full diagonalization by hand, the conceptual picture matters.

## When diagonalization is possible

An `n x n` matrix is diagonalizable if it has `n` linearly independent eigenvectors.

This always happens when the matrix has `n` distinct eigenvalues.

But distinct eigenvalues are sufficient, not necessary. Some matrices with repeated eigenvalues are still diagonalizable.

For example,

```text
[2 0]
[0 2]
```

has a repeated eigenvalue `2`, but every nonzero vector is an eigenvector, so it is certainly diagonalizable.

## When diagonalization fails

Consider

```text
J = [2 1]
    [0 2]
```

This matrix has only one eigenvalue, `2`, and only one independent eigenvector.

So it cannot be diagonalized.

The matrix is still meaningful, but it cannot be fully uncoupled into independent eigenvector directions.

That is an important limitation.

## Similarity

Matrices `A` and `D` related by

`A = P D P^-1`

are called similar.

Similar matrices represent the same linear transformation in different bases.

So diagonalization is not changing the transformation. It is changing the coordinates used to describe it.

## An example of long-term behavior

Suppose `A` has eigenvalues `3` and `1/2`, with independent eigenvectors `v_1` and `v_2`.

If

`x_0 = 4v_1 - 7v_2`

then

`x_k = 4(3^k)v_1 - 7(1/2)^k v_2`

As `k` grows:

- the `v_1` part explodes
- the `v_2` part disappears

Eventually the state points almost entirely in the `v_1` direction.

This is why the eigenvalue of largest magnitude often dominates a system.

## Markov-style intuition

Some matrices are used to move probabilities around. In those cases the largest eigenvalue is often `1`, and the associated eigenvector represents a steady state.

That topic appears again when studying networks and Markov chains, but the diagonalization idea is already visible:

- eigenvalue `1` means a direction that stays fixed in size
- smaller magnitudes decay away
- the stable long-term pattern is tied to the dominant eigendirection

## Oscillation

If an eigenvalue is negative, repeated powers alternate sign.

For instance, if `lambda = -2`, then

- `lambda^1 = -2`
- `lambda^2 = 4`
- `lambda^3 = -8`

So a component along that eigenvector flips direction every step while growing in magnitude.

If `lambda = -1`, the system oscillates without growing or shrinking along that direction.

## Diagonalization and differential equations preview

Diagonalization is useful not only for discrete systems but also for continuous ones.

In differential equations of the form

`x'(t) = A x(t)`

eigenvalues again control growth, decay, and oscillation. Diagonalization helps decouple the system into simpler scalar equations.

We will return to this later in the book.

## How to diagonalize in practice

Here is the standard workflow:

1. Compute the eigenvalues of `A`.
2. For each eigenvalue, find a basis for its eigenspace.
3. Check whether you have enough independent eigenvectors to form a basis.
4. Build `P` from those eigenvectors.
5. Build `D` from the corresponding eigenvalues in the same order.
6. Use `A = PDP^-1`.

Order matters: the `i`th column of `P` must match the `i`th diagonal entry of `D`.

## Common mistakes

### Mistake 1: mixing the order of eigenvectors and eigenvalues

If the first column of `P` is `v_1`, then the first diagonal entry of `D` must be the eigenvalue associated with `v_1`.

### Mistake 2: assuming every matrix is diagonalizable

Some matrices simply do not have enough independent eigenvectors.

### Mistake 3: forgetting the meaning of `P^-1`

`P^-1` is not a random algebraic object. It converts ordinary coordinates into coordinates relative to the eigenvector basis.

### Mistake 4: using eigenvalues alone to describe everything

Eigenvalues are crucial, but the eigenvectors and the decomposition of the initial condition matter too.

## A small comparison table

| Matrix type | Behavior |
|---|---|
| Diagonal | already uncoupled |
| Diagonalizable | uncoupled after a change of basis |
| Not diagonalizable | cannot be fully uncoupled by eigenvectors alone |

## A concept picture

```text
original state x0
    |
    v
write x0 in eigenvector basis
    |
    v
scale each component by powers of eigenvalues
    |
    v
reassemble into xk
```

This is the whole logic of linear dynamics in diagonalizable systems.

## Recap

Diagonalization rewrites a matrix as

`A = P D P^-1`

where `D` is diagonal and `P` contains eigenvectors.

This matters because:

- diagonal matrices are easy to understand
- powers become `A^k = P D^k P^-1`
- discrete dynamics `x_{k+1} = A x_k` become easy to analyze
- long-term behavior is controlled by eigenvalue magnitudes

In the right basis, a complicated transformation often turns into simple coordinate-wise scaling.

That is the real meaning of diagonalization.

## Exercises

1. Explain in words why diagonal matrices are easy to raise to powers.

2. If

```text
D = [3 0]
    [0 2]
```

compute `D^4`.

3. Suppose `A = PDP^-1`. Show that `A^2 = PD^2P^-1`.

4. A matrix has eigenvalues `0.8` and `1.3`. What can you say about the long-term behavior of `x_{k+1} = A x_k`?

5. Why does a matrix with distinct eigenvalues always diagonalize?

6. Give an example of a repeated eigenvalue matrix that is diagonalizable.

7. Give an example of a repeated eigenvalue matrix that is not diagonalizable.

8. Suppose `x_0 = 2v_1 + 5v_2`, where `v_1` and `v_2` are eigenvectors with eigenvalues `4` and `1/3`. Write a formula for `x_k`.

9. A system has eigenvalues `-1` and `1/2`. Describe the qualitative behavior along each eigendirection.

10. In your own words, explain why diagonalization is really about choosing the right coordinates.
