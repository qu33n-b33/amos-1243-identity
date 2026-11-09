# The Amos 1243 Identity

**Elizabeth Victoria Amos · Founder, Arraxiom Labs**  
**Discovery recorded November 2, 2026 · North Carolina, USA**

I arrived at this expression while experimenting with numbers I chose
because of Jesse. I named it the Amos 1243 Identity.

## Statement

For every nonzero real number $x$,

$$
f(x) = \frac{x}{x/1028} + 215 = 1243.
$$

## How it works

Divide $x$ by 1028. This gives exactly one 1028th of $x$.
Now divide the original $x$ by that fraction of itself. The quotient
is 1028. Adding 215 gives 1243.

## Proof

Since $x \ne 0$, the denominator $x/1028$ is nonzero. Dividing
by it is equivalent to multiplying by its reciprocal.

$$
\begin{aligned}
f(x)
  &= x \cdot \frac{1028}{x} + 215 \\
  &= 1028 + 215 \\
  &= 1243.
\end{aligned}
$$

At $x = 0$, the original expression contains $0/0$ and is undefined.

## Worked examples

| Input | Substitution | Result |
| ---: | :--- | ---: |
| 7 | `7 / (7 / 1028) + 215` | 1243 |
| 83 | `83 / (83 / 1028) + 215` | 1243 |
| −19 | `(-19) / ((-19) / 1028) + 215` | 1243 |
| 3.5 | `3.5 / (3.5 / 1028) + 215` | 1243 |
| 2003 | `2003 / (2003 / 1028) + 215` | 1243 |

## General form

The same cancellation gives $x/(x/a) + b = a + b$ for nonzero
real $x$ and $a$. My expression uses $a = 1028$ and $b = 215$.

## Run the examples

Run `python3 amos_1243.py` from the repository folder.
The script uses Python's standard library and verifies the examples
with exact rational arithmetic.

*For Jesse.*
