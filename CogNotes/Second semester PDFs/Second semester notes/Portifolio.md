1)
a) (2,3,1) = 6
b) (-1,-1,2) = 0
c) (-2,-3,2) = -3
d) (-2, 1, 1)
e) (3,-3,0)
f) (7, -5, 1)

2)
a)

We know that $\vec{u} \ \times \ \vec{v}$ is ⊥ to both $\vec{u} \ and \ \vec{v}$. So, $\vec{u} \ \times \ \vec{v} = (-2,1,2)= \vec{cross}$ . 
We then need to express $\vec{cross}$ as a unit vector.
$\sqrt{(-2)^2+1^2+2^2}= \sqrt9 = 3$, therefore we can find the unit vector as $\vec{unit} = (\frac{-2}{3}\frac{1}{3}\frac{2}{3})$, and it keeps its perpendicular properties as we only transform it by scaling it down.
$\sqrt{((-2/3)^2+(1/3)^2+(2/3)^2)}=1$.
 

$$\sqrt{x^2+y^2+z^2}=1$$
$$(x*1+y*0+z*1)=0$$
$$(x*1+y*2+z*0)=0$$

b)
$\vec{u_1} \ \times \ \vec{u_2} = (-3,1,3)= \vec{u_{\times}}$. We have to scale the vector so that the following is true: $\vec{u_{\times}}*\vec{v}=8$,   but as $\vec{v}$ is (1,1,0) the dot product will only be negative numbers, but if we multiply the cross-product-vector by a a negative number it will keep its dimensional properties and allow for a positive dot product.

Find scaler x for the following is true:
$-3x + 1x = 8 \iff  -2x=8 \iff x = -4$
So the vector is $$-4*\vec{u_{\times}} = \begin{pmatrix}
-3 \cdot -4 \\
1 \cdot -4  \\
4 \cdot -4  \\
\end{pmatrix} = \begin{pmatrix}
12 \\
-4  \\
12  \\
\end{pmatrix}$$

3)


$$ \begin{pmatrix}
0 \ 0 \ 1 \\
0 \ 1 \ 0 \\
1 \ 0 \ 1 \\
\end{pmatrix}^2
=\begin{pmatrix}
0 \ 0 \ 1 \\
0 \ 1 \ 0 \\
1 \ 0 \ 1 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
0 \ 0 \ 1 \\
0 \ 1 \ 0 \\
1 \ 0 \ 1 \\
\end{pmatrix}
=
\begin{pmatrix}
1 \ 0 \ 0  \\
0 \ 1 \ 0 \\
1 \ 0 \ 1 \\
\end{pmatrix}$$

For the matrix
$$
X = \begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{bmatrix}^n 
$$

calculate $X^n$ for $n = 2, 3,4, 5$. Write a rule for calculating higher values of $n$.

**Rule for calculating higher values:**
Given that $F_0 = 0 \ and \ F_1 = 1$ and $F_n = F_{n-1}+F_{n-2}$, we can describe the scalars of the matrix as $F_n$



$$
X = \begin{bmatrix}
F_{n-1} & 0 & F_n \\
0 & 1 & 0 \\
F_n & 0 & F_{n+1}
\end{bmatrix},
$$



