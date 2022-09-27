Written by: Laurits Lyngbæk
Source of information: [[Gill chapter 3.pdf]]
Association links: [[103 Methods 2]]
Tags: #🌿Sprout 
___
# Linear Algebra
**Vectors, Matrices, and Operations**
This markdown will focus on the **mechanics** of vectors and matrices.
This involves learning to perform operations on vectors and matrices, but also getting an overview of vectors as a mathematical concept, where the values have a significant meaning.

## Operations
The mechanical operations of linear algebra is the most simple algebraic steps:

```ad-example
title: Vector opearation on *conformable* vectors
The following examples uses the following vectors:
$\vec{u} = [3,3,3,3]$ and $\vec{v} = [1,2,3,4]$
!!! ad-info
    title: Addition
$$\vec{u} + \vec{v} = [u_1 + v_1, u_2 + v_2, u_3 + v_3, u_4 + v_4] = [4, 5, 6, 7]$$

	
!!! ad-info
    title: Substraction
$$\vec{u} − \vec{v} = [u_1 − v_1, u_2 − v_2, u_3 − v_3, u_4 − v_4] = [2, 1, 0,−1]$$
!!! ad-info
    title: Multiplication
$$3 × \vec{v} = [3 × v_1, 3 × v_2, 3 × v_3, 3 × v_4] = [3, 6, 9, 12]$$
!!! ad-info
    title: Division
$$\vec{v}/3 = [v_1 /3, v_2 /3, v_3 /3, v_4 /3] =[\frac13 , \frac23 , 1, \frac43]$$

!!! ad-info
    title: Dot Product (vector inner product)
![[Dot product definition.png]]
![[Dot product example.png]]	



**These are the formal operations of dot products**
![[Dot product operations 1.png]]

!!! ad-info
    title: Vector Cross Product (vector outer product)
![[Cross product.png]]	
![[cross product visual.png]]
![[Right hand rule.png]]
	The cross product $w$ is actually the [[determinant]]
	Cross products are seldom usefull in cognitive science, as we dont do geometry.
**These are the formal operations of cross products**
![[Formal cross product operations 1.png]]

```

Conformable vectors are two vectors of the same length
Consider the vectors u, v, w, which are identically sized, and the scalars s and
t. The following intuitive properties hold.
![[Vector operations 1.png]]

## Vector
A **vector** is just a serial listing of numbers where the order matters.
E.g. we can store the first four positive integers in a vectors:
	In a row vector: $v = [1,2,3,4]$ 
	In a column vector: $\vec{v}=\begin{bmatrix} 1 \\ 2 \\ 3 \\ 4  \end{bmatrix}$ 
The numbers **inside** the vector, are called **scalars**. In the up above example the **scalars** would be 1,2,3, and 4
	

### Length of a vector (vector norm):
	
![[Vector norms.png]]
	
![[Properties of vector norms.png]]




## Matrix
A **matrix** is a rectangular arrangement of numbers:
It is a way to **individually assign numbers**, now called **matrix elements** or **entries**, to specified positions in a **single structure**, referred to with a **single name**.

As opposed to vector where ordering matters, in a matrix both **ordering in columns and rows matters**. 

**Matrices** have **two definable dimensions**, the number of rows and the number
of columns, whereas vectors only have one, and we **denote matrix size** by
$row \space × \space column$.
$$x_{n × m}=
\begin{bmatrix}
x_{11} & \ldots & x_{1n}\\ 
\vdots  & \ddots & \vdots\\
 x_{m1}& \ldots & x_{mn}
\end{bmatrix}$$



Covariance matrixes will be symmetric and positive definite.

### Properties of matrix manipulation:
![[Properties of (Conformable) Matrix Manipulation.png]]
### Matrix operations praxis:
```ad-info
title: Matrix Addition
```
![[Matrix addition.png]]
```ad-info
title: Matrix Subtraction
```
![[Matrix substraction.png]]
```ad-info
title: Matrix Scalar Multiplication
```
![[Matrix Scalar Multiplication.png]]
```ad-info
title: Matrix Scalar Division
```
![[Matrix Scalar Division.png]]

### Conform Matrix Manipulation
```ad-info
title: Conform Matrix Multiplication
```
Matrix multiplication is necessarily more complicated than these simple operations:
The first issue is **conformability**: **Two matrices** are conformable for multiplication **if** the number of **columns in the first** matrix match the number of **rows in the second matrix**.
These ***matrixes are conform***, as the inner numbers match: 
![[Conform matrixes.png]]
However, these ***matrixes are ==not== conform***, unless $p = k$:
![[not conform matrixes.png]]
The resulting matrix XY will be of the size of the **"outer numbers"** (kn)(np) will become kp
Multiplying with a matrix that is first is called pre-multiplication (pre-matrix*post-matrix)


**Matrix multiplication in praxis:**
See http://matrixmultiplication.xyz/
$$
\begin{bmatrix}
1 & \frac12 & 2\\ 
1 & \frac13 & 5\\ 
1 & 1 & 2
\end{bmatrix}
\begin{bmatrix}
0.1 \\ 
0.2 \\ 
0.3
\end{bmatrix}
=
\begin{bmatrix}
1*0.1 + \frac12*0.2 +2*0.3\\ 
1*0.1 + \frac13*0.2 +5*0.3\\ 
1*0.1 + 1*0.2 +2*0.3
\end{bmatrix}
=
\begin{bmatrix}
0.1 + 0.1 +0.6\\ 
0.1 + 1/15 + 1.5\\ 
0.1 + 0.2 +0.6
\end{bmatrix}
\begin{bmatrix}
0.8\\ 
1.67\\ 
0.9
\end{bmatrix}
$$


#### Properties of conform matrix manipulation

![[Properties of (Conformable) Matrix Multiplication.png]]
### Properties of Matrix Transposition:
![[Properties of Matrix Transposition.png]]
![[Matrix Transposition praxis.png]]
