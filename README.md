# The Chinese Remainder Theorem
This repository presents different implementations for solving systems of linear congruences in Python. It includes the classical version of the Chinese Remainder Theorem, with an asymptotic cost of $\Theta(n^2)$; an algorithm that maintains the verification of coprime modules from the original theorem, with a cost of $O(n^2 \cdot \log(\min(a,b))))$; and also proposes an algorithm that eliminates the need for module verification, reducing the complexity to $O(n \cdot \log(\min(a,b))))$.

## Requirements
- [x]  Python programming language
- [x]  Numpy library

To install Numpy, use the following command:

```
pip install numpy
```
## Installation
To clone the repository, use the following command:
```
git clone https://github.com/anacarlaquallio/chinese-remainder-theorem/
```

## About the Chinese Remainder Theorem
The Chinese Remainder Theorem is a method that solves systems of pairwise linear congruences in the form:

$x \equiv A_1 \pmod{m_1}$

$x \equiv A_2 \pmod{m_2}$

$\vdots$

$x \equiv A_n \pmod{m_n}$

Where $m_1, m_2, \ldots, m_n$ are coprime. 

***

### Classical Chinese Remainder Theorem
| $A$      | $M$      | $\overline{M}$      | $\overline{M^{-1}}$   | $A \cdot M \cdot \overline{M^{-1}}$        |
|--------|--------|----------------------|---------------------------|---------------------------------------|
| $A_1$  | $M_1$  | $\overline{M_1}$    | $\overline{M_1^{-1}}$     | $A_1 \cdot M_1 \cdot \overline{M_1^{-1}}$  |
| $\vdots$ | $\vdots$ | $\vdots$         | $\vdots$                 | $\vdots$                                   |
| $A_n$  | $M_n$  | $\overline{M_n}$    | $\overline{M_n^{-1}}$     | $A_n \cdot M_n \cdot \overline{M_n^{-1}}$  |

Where $M$ is the product of $m_1, m_2, \ldots, m_n$ excluding the corresponding row; $\overline{M}$ is the equivalence class of $M$ with respect to the modulus of the current row, and $\overline{M^{-1}}$ is the inverse of $\overline{M}$.

***

### Proposal for the Chinese Remainder Theorem (module coprime)
The developed method that provides a solution for systems of modular congruences resolves pairwise, and initially, the modules are coprime, just like the Chinese Remainder Theorem. Under such an optic, consider the system:


$mx \equiv a \pmod{b}$

$nx \equiv c \pmod{d}$



If $m$ is different from $1$, it is necessary to find the multiplicative inverse of $m$ modulo $b$, that is, $m^{-1} \pmod{b}$. The same applies to $n$, in the case of $n^{-1} \pmod{d}$. Next, equations must be multiplied by their respective inverses to get $1x$. Thus, the formula can be used:

$x = \left[b^{-1}\pmod{d}\cdot b \cdot (c - a) + a \right] \pm b \cdot d \cdot \gamma$

Resulting in a set of possibilities that satisfy the system of linear congruences. The proposed method also finds solutions for systems with non-coprime modules. To solve it, consider $j = \text{gcd}(b,d)$ and divide the numbers $b$ and $d$ by $j$, such as $b = \frac{b}{j}$ and $d = \frac{d}{j}$. Finally, the formula is written as:

$x = \left[b^{-1}\pmod{d}\cdot b \cdot (c - a) + a \right] \pm b \cdot d \cdot j \cdot \gamma$

## Authors

* **Ana Carla Quallio Rosa**
* **Fernando Cézar Gonçalves Manso**
* **Juliano Henrique Foleiss**
* **Wellington José Corrêa**
