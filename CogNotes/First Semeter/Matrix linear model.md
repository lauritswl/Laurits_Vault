## Vectors and matrices
### Vectors 
Vectors are a list of numbers

| Latex                                             | Output                                                |
| ------------------------------------------------- | ----------------------------------------------------- |
| \vec{x}$$                                           | $\vec{x}$                                             |
| \begin{bmatrix} 1 \\ 2 \\ ... \\ n  \end{bmatrix} | $\begin{bmatrix} 1 \\ 2 \\ ... \\ n  \end{bmatrix}$ |
|                                                   |                                                       |



**You can have multiple linear models connected as a matrix linear model:**



$$ \begin{bmatrix} y_1=\beta_0+\beta_1x_1 \\ y_2=\beta_0+\beta_1x_2 \\ y_....=\beta_0+\beta_1x_.... \\ y_n=\beta_0+\beta_1x_n \end{bmatrix}$$
$$\vec{y}=\begin{bmatrix}y_1 \\ y_2 \\ ... \\ y_n\end{bmatrix} -> \vec{b}=\begin{bmatrix}\beta_0\\ \beta_1\end{bmatrix}$$
$$\vec{y}=X*\vec{\beta}+\vec{\epsilon}$$


Example of multiplying a vector by a matrix
$$\hat{y}=X\hat{\beta}$$
$$\vec{y}=
\begin{bmatrix} 43.3\\46.3\\55.3\end{bmatrix}=
\begin{bmatrix} 1 & -1\\ 1&0 \\ 1&3 \end{bmatrix}
\begin{bmatrix} 46.3 \\ 3.0\end{bmatrix}$$