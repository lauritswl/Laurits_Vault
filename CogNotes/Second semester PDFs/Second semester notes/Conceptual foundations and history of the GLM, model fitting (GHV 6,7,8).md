Written by: Laurits Lyngbæk
Source of information: [[Methods ROS.pdf|Regression and Other Stories by Gelman, Hill, and Vehtari (2020), chp 6,7,8]]
Association links: [[103 Methods 2]]
Tags: #🌲Evergreen 
___
# Conceptual foundation of General Linear Model

**Description of a general linear model as vectors/matrixes:**

$$\vec{y}=X \vec{\hat{\beta}}+\vec{\epsilon}$$
$$
\begin{bmatrix}y_1 \\ y_2 \\ ... \\ y_n\end{bmatrix}
= \begin{bmatrix}1 & x_1 \\ 1 & x_2 \\ ... & ... \\ 1 & x_n\end{bmatrix}
\cdot \begin{bmatrix}\beta_{0} \\ \beta_1\end{bmatrix}
+\begin{bmatrix}\epsilon_1 \\ \epsilon_2 \\ ... \\ \epsilon_n\end{bmatrix}
$$
**Sum of squares: loss function**
$$
\sum_{i=-1}^{n} \epsilon_{i}^{2}= \vec{\epsilon} \cdot \vec{\epsilon} = \begin{bmatrix}\epsilon_1 & \epsilon_2 & ... & \epsilon_i\end{bmatrix}\begin{bmatrix}\epsilon_1 \\ \epsilon_2 \\ ... \\ \epsilon_i\end{bmatrix}
$$
**We need to optimize this function of error loss:**
$$\vec{y}=X \vec{\hat{\beta}}+\vec{\epsilon} \iff \vec{y}-X \vec{\hat{\beta}}=\vec{\epsilon}$$
$$\begin{aligned}
0 = \frac{\partial}{\partial\beta} \space \epsilon^{T\epsilon} 
\\
0 = \frac{\partial}{\partial \beta}(y-X\hat\beta)(y-X\hat\beta)
\\
0 = -X^Ty+X^TX\hat\beta
\\
X^TX\hat\beta=X^Ty
\\
\hat\beta=(X^TX)^{-1}X^Ty
\end{aligned}$$

