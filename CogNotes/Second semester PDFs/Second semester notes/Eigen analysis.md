### Eigen analysis
Eigenanalysis is a mathematical operation on a square, symmetric matrix. 
**A square matrix** has the same number of rows as columns.
**A symmetric matrix** is the same if you switch rows and columns.
<iframe src="https://www.geogebra.org/m/JP2XZpzV" width="100%" height="300" style="border:1px solid black;">  
</iframe>

**Find lambda (eigen values/vector):**
$$\begin{bmatrix}5 & 3 \\ 2 & 4\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
=\lambda\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
=\begin{bmatrix}\lambda & 0 \\ 0 & \lambda\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}$$
$$\begin{bmatrix}5 & 3 \\ 2 & 4\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
-\lambda\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
=\begin{bmatrix}5 & 3 \\ 2 & 4\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
-\begin{bmatrix}\lambda & 0 \\ 0 & \lambda\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
=0$$
$$(\begin{bmatrix}4 & 3 \\ 2 & 4\end{bmatrix}-\begin{bmatrix}\lambda & 0 \\ 0 & \lambda\end{bmatrix})\begin{bmatrix}u_1 \\ u_2\end{bmatrix}=0$$
$$\begin{bmatrix}5-\lambda & 3 \\ 2 & 4-\lambda\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}=0$$

If $\begin{bmatrix}u_1 \\ u_2\end{bmatrix}$ is non-zero then we can solve for λ using just the determinant:
$$det\begin{bmatrix}5-\lambda & 3 \\ 2 & 4-\lambda\end{bmatrix}=0=(5-\lambda)(4-\lambda)-2*3=20-5\lambda-4\lambda+\lambda^2-6=\lambda^2-9\lambda+14$$
$$0=\lambda^{2}-9\lambda+14\iff \lambda= \begin{bmatrix}7 \\ 2\end{bmatrix}$$
You can insert either 7 or 2, to find your eichenvector:
$$\begin{bmatrix}5 & 3 \\ 2 & 4\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
=\lambda\begin{bmatrix}u_1 \\ u_2\end{bmatrix}$$
=>
$$\begin{bmatrix}5 & 3 \\ 2 & 4\end{bmatrix}\begin{bmatrix}u_1 \\ u_2\end{bmatrix}
=7\begin{bmatrix}u_1 \\ u_2\end{bmatrix}$$
$$\begin{bmatrix}5u_1+3u_2=7u_1 \\ 2u_1+4u_2=7u_2\end{bmatrix}$$
$$\begin{bmatrix}3u_2 =2u_1 \\ 2u_1=3u_2\end{bmatrix}$$
We now have the correlation for the eichenvector, we can use a vector of any length, but the ecuation still has to be true. 
$$\begin{bmatrix}5 & 3 \\ 2 & 4\end{bmatrix}\begin{bmatrix}3 \\ 2\end{bmatrix}=\begin{bmatrix}21 \\ 14\end{bmatrix}$$
$$\begin{bmatrix}5 & 3 \\ 2 & 4\end{bmatrix}\begin{bmatrix}-1 \\ -\frac{2}{3}\end{bmatrix}=\begin{bmatrix}-7 \\ -\frac{14}{3}\end{bmatrix}$$
For these two eichen vectors, the u1 and u2 value correlation is true, and its therefore eichen vectors.


## Rotation of matrix
Vector you have to multiply with for rotation:
$$\begin{bmatrix}cos(\psi) & -sin(\psi) \\ sin(\psi) & cos(\psi)\end{bmatrix}$$

90 degree rotation:

$$\begin{bmatrix}cos(90) & -sin(90) \\ sin(90) & cos(90)\end{bmatrix}
\begin{bmatrix}X_1 & X_2 \\ X_3 & X_4\end{bmatrix}
=\begin{bmatrix}0 & -1  \\  1 & 0\end{bmatrix}
\begin{bmatrix}X_1 & X_2 \\ X_3 & X_4\end{bmatrix}$$
