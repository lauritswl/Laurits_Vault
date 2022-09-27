Written by: Laurits Lyngbæk
Source of information: [[Gill chapter 4.pdf]]
Association links: [[103 Methods 2]]
Tags: #🌿Sprout 
___
# More linear algebra
## Recap from last [[Linear Algebra _ Vectors, Matrices, and Operations| Linear Algebra]]
If the dot product of two vectors = 0, they are orthogonal (vinkelret). 
You can find a vector that is orthogonal to two vectors, by finding their cross product.
You can find the norm (length of a vector) by $\sqrt{x^2+b^2+c^2}$

## Projections
We can project a vector $\vec{v}$ against another vector $\vec{u}$ with the following formula:

$$p=projection \ of \ \vec{v}\ on\ to\ \vec{u}=\left(\frac{\vec{u} 
\cdot \vec{v}}{|| \vec{u}||}\right)\cdot (\frac{\vec{u}}{|| \vec{u}||}) $$
To get a visual understanding look at this visual example of Projection (p), Addition (v+u) and Subtraction (v-u).
## Matrixes
One of the best ways to summarize a matrix is by its determinant:

Visual representation of a determinant of a 2 by 2 matrix:
![[Matrix determinant exca]]

The **determinant** is $ad-bc$ and is the **area** of the *extended parallelogram of the vectors*.


Try and prove the determinant is 14:

$$\begin{pmatrix}5 & 3 \\2 & 4\\ \end{pmatrix}$$

Inverse of a 2x2 matrix:

$$for: X\begin{pmatrix}a & b  \\ c & d\end{pmatrix}, \ the \ inverse \ matrix \ is\ X^{-1}=\frac{1}{detX} \cdot \begin{pmatrix}d & -b \\ -c & a\end{pmatrix}$$



**Day trip**
Find out how many children and adults goes on the trip:

Out: 30 kr for a child
32 kr for a adult
total: 1184 kr

In:
35 child
36 child
total 1352 kr
$$X =\begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}$$
$$X =\begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}$$
I: $30x_1+32x_2=1184$
II: $35x_1+36x_2=1352$
$\begin{pmatrix}30 & 32 \\ 35 & 36\end{pmatrix}\begin{pmatrix}x_1 \\ x_2\end{pmatrix}=\begin{pmatrix}1184 \\ 1352\end{pmatrix}$
=> $\begin{pmatrix}x_1 \\ x_2\end{pmatrix}=\begin{pmatrix}30 & 32 \\ 35 & 36\end{pmatrix}^{-1}\begin{pmatrix}1184 \\ 1352\end{pmatrix}$
**Need to add 1/determinant!!:**
=> $\begin{pmatrix}x_1 \\ x_2\end{pmatrix}=\frac{1}{detX}\begin{pmatrix}36 & -32 \\ -35 & 30\end{pmatrix}\begin{pmatrix}1184 \\ 1352\end{pmatrix}$
=> $\begin{pmatrix}x_1 \\ x_2\end{pmatrix}= \begin{pmatrix}36*1184 + (-32*1352) \\ -35*1184 + 30*1352\end{pmatrix}$ = $\begin{pmatrix}42624-43264 \\ -41440+40560\end{pmatrix}$ = $\begin{pmatrix}-740 \\ -880\end{pmatrix}$





