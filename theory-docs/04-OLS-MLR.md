# Derivation of the Ordinary Least Squares Estimator for Multiple Regression

$y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + \varepsilon_i.$

where
- $\beta_0$: is the interception
- $\varepsilon_i$: Error term

## 1. Model setup

We have $n$ observations and $p$ predictors. In vector/matrix form:

$$
y =
\begin{pmatrix}
y_1\\
\vdots\\
y_n
\end{pmatrix},\quad
X =
\begin{pmatrix}
1 & x_{11} & \dots & x_{1p}\\
1 & x_{21} & \dots & x_{2p}\\
\vdots & \vdots &      & \vdots\\
1 & x_{n1} & \dots & x_{np}
\end{pmatrix},\quad
\beta =
\begin{pmatrix}
\beta_0\\
\beta_1\\
\vdots\\
\beta_p
\end{pmatrix}.
$$

so that our fitted values are $\hat y = X\beta$ and the residuals are $r = y - X\beta$.

> Why a column of 1’s?

In multiple regression we write our predictions as  
$$y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip}$$  
To capture the constant term $\beta_0$ in matrix form, we prepend a column of 1’s to $X$:

$$
X = 
\begin{pmatrix}
\color{gray}{1} & x_{11} & \dots & x_{1p}\\
\color{gray}{1} & x_{21} & \dots & x_{2p}\\
\vdots         & \vdots &      & \vdots\\
\color{gray}{1} & x_{n1} & \dots & x_{np}
\end{pmatrix},\quad
\beta =
\begin{pmatrix}
\beta_0\\
\beta_1\\
\vdots\\
\beta_p
\end{pmatrix}.
$$

---

## 2. Ordinary least squares criterion

We choose $\hat\beta$ to minimize the sum of squared residuals:

$$
S(\beta)
= (y - X\beta)^\top\,(y - X\beta)
= \sum_{i=1}^n \bigl(y_i - x_i^\top\beta\bigr)^2.
$$

### Detailed proof

1. **Define the residual vector**  
   Let  
   $$
   r = y - X\beta
     = \begin{pmatrix}r_1\\\vdots\\r_n\end{pmatrix},
   $$  
   where each residual is  
   $$
   r_i = y_i - x_i^\top\beta.
   $$

2. **Rewrite in dot‐product form**  
   By definition of the transpose,
   $$
   (y - X\beta)^\top(y - X\beta) = r^\top r.
   $$

3. **Expand the dot‐product**  ($\sum_{i=1}^n r_i^2$ is sum of residual square)
   
   For any vector $r$,  
   $$
   r^\top r
   = \sum_{i=1}^n r_i \, r_i
   = \sum_{i=1}^n r_i^2.
   $$

4. **Substitute the residuals**  
   Since $r_i = y_i - x_i^\top\beta$,  
   $$
   r^\top r
   = \sum_{i=1}^n (y_i - x_i^\top\beta)^2.
   $$

Putting it all together,  
$$
S(\beta)
= (y - X\beta)^\top(y - X\beta)
= \sum_{i=1}^n \bigl(y_i - x_i^\top\beta\bigr)^2,
$$  
as required.

### Example

Let’s take $n=2$ observations with

$$
y = \begin{pmatrix}3\\5\end{pmatrix},\quad
X\beta = \begin{pmatrix}2\\4\end{pmatrix}.
$$

1. **Compute the residual vector**  
   $$
   r = y - X\beta
     = \begin{pmatrix}3\\5\end{pmatrix}
       - \begin{pmatrix}2\\4\end{pmatrix}
     = \begin{pmatrix}1\\1\end{pmatrix}.
   $$

2. **Form the dot‐product**  
   $$
   r^\top r
   = \begin{pmatrix}1 & 1\end{pmatrix}
     \begin{pmatrix}1\\1\end{pmatrix}
   = 1\cdot1 + 1\cdot1
   = 2.
   $$

3. **Compare to the sum of squares**  
   $$
   \sum_{i=1}^2 r_i^2
   = 1^2 + 1^2
   = 2.
   $$

Hence in this toy example,

$$
(y - X\beta)^\top(y - X\beta)
= r^\top r
= \sum_{i=1}^2 r_i^2,
$$

demonstrating step 2.  

---

## 3. Expand $S(\beta)$

Using $(A - B)^\top = A^\top - B^\top$ and $(AB)^\top = B^\top A^\top$, we get

$$
\begin{aligned}
S(\beta)
&= (y - X\beta)^\top(y - X\beta) \\
&= y^\top y
  - y^\top(X\beta)
  - (X\beta)^\top y
  + (X\beta)^\top(X\beta) \\
&= y^\top y
  - \beta^\top X^\top y
  - \beta^\top X^\top y
  + \beta^\top X^\top X\,\beta \\
&= y^\top y
  - 2\,\beta^\top X^\top y
  + \beta^\top (X^\top X)\,\beta.
\end{aligned}
$$

---

## 4. Compute the gradient $\nabla_\beta S$

- $\displaystyle \frac{\partial}{\partial\beta}\!\bigl(c^\top\beta\bigr) = c$  
- $\displaystyle \frac{\partial}{\partial\beta}\!\bigl(\beta^\top A\beta\bigr) = (A + A^\top)\beta$, and since $X^\top X$ is symmetric this is $2X^\top X\,\beta$

$$
\begin{aligned}
\nabla_\beta S
&= \frac{\partial}{\partial\beta}\bigl[y^\top y\bigr]
  + \frac{\partial}{\partial\beta}\bigl(-2\,\beta^\top X^\top y\bigr)
  + \frac{\partial}{\partial\beta}\bigl(\beta^\top X^\top X\,\beta\bigr) \\
&= 0 \;-\;2\,X^\top y \;+\;2\,X^\top X\,\beta.
\end{aligned}
$$

### Detailed proof

We start from the expanded form:  
$$
S(\beta)
= y^\top y
\;-\;2\,\beta^\top X^\top y
\;+\;\beta^\top X^\top X\,\beta.
$$

---

1. **Derivative of the constant term**  
   Since $y^\top y$ does not depend on $\beta$,  
   $$
   \frac{\partial}{\partial\beta}\bigl(y^\top y\bigr)
   = 0.
   $$

2. **Derivative of the linear term**  
   Write  
   $$
   -2\,\beta^\top X^\top y
   = -2\,(X^\top y)^\top \beta
   = -2\,c^\top \beta,
   \quad c = X^\top y.
   $$  
   A standard result gives  
   $$
   \frac{\partial}{\partial\beta}\!\bigl(c^\top \beta\bigr)
   = c.
   $$  
   Therefore  
   $$
   \frac{\partial}{\partial\beta}\!\bigl(-2\,\beta^\top X^\top y\bigr)
   = -2\,c
   = -2\,X^\top y.
   $$

3. **Derivative of the quadratic term**  
   Let $A = X^\top X$.  The term is  
   $$
   \beta^\top A\,\beta.
   $$  
   By matrix‐calculus,  
   $$
   \frac{\partial}{\partial\beta}\!\bigl(\beta^\top A\,\beta\bigr)
   = (A + A^\top)\,\beta.
   $$  
   Since $A$ is symmetric, by definition $A = A^\top$. Hence,
   $$
    A + A^\top = A + A = 2A.
   $$
   this simplifies to  
   $$
   2\,X^\top X\,\beta.
   $$

4. **Combine all pieces**  
   $$
   \begin{aligned}
   \nabla_\beta S
   &= \frac{\partial}{\partial\beta}\bigl(y^\top y\bigr)
     + \frac{\partial}{\partial\beta}\bigl(-2\,\beta^\top X^\top y\bigr)
     + \frac{\partial}{\partial\beta}\bigl(\beta^\top X^\top X\,\beta\bigr) \\
   &= 0 \;-\;2\,X^\top y \;+\;2\,X^\top X\,\beta.
   \end{aligned}
   $$

Hence  
$$
\boxed{\nabla_\beta S = -2\,X^\top y + 2\,X^\top X\,\beta.}
$$

---

## 5. Set the gradient to zero → normal equations

$$
-2\,X^\top y + 2\,X^\top X\,\beta = 0
\quad\Longrightarrow\quad
X^\top X\,\beta = X^\top y.
$$

---

## 6. Closed-form solution

Assuming $X^\top X$ is invertible:

$$
\boxed{
\hat\beta = (X^\top X)^{-1}\,X^\top y.
}
$$

---

## 7. Numeric example: detailed step-by-step

Let \(n=3\), \(p=2\):

$$
X = \begin{pmatrix}
1 & 0 & 1\\
1 & 1 & 0\\
1 & 1 & 1
\end{pmatrix},\quad
y = \begin{pmatrix}1\\2\\3\end{pmatrix}.
$$

### Step 1: Compute $X^\top X$

First write  
$$
X^\top = \begin{pmatrix}
1 & 1 & 1\\
0 & 1 & 1\\
1 & 0 & 1
\end{pmatrix}.
$$  
Then $(X^\top X)_{ij} = \sum_{k=1}^3 X_{k,i}\,X_{k,j}$:

$$
\begin{aligned}
(X^\top X)_{11} &= 1\cdot1 + 1\cdot1 + 1\cdot1 = 3,\\
(X^\top X)_{12} &= 1\cdot0 + 1\cdot1 + 1\cdot1 = 2,\\
(X^\top X)_{13} &= 1\cdot1 + 1\cdot0 + 1\cdot1 = 2,\\
(X^\top X)_{21} &= 0\cdot1 + 1\cdot1 + 1\cdot1 = 2,\\
(X^\top X)_{22} &= 0\cdot0 + 1\cdot1 + 1\cdot1 = 2,\\
(X^\top X)_{23} &= 0\cdot1 + 1\cdot0 + 1\cdot1 = 1,\\
(X^\top X)_{31} &= 1\cdot1 + 0\cdot1 + 1\cdot1 = 2,\\
(X^\top X)_{32} &= 1\cdot0 + 0\cdot1 + 1\cdot1 = 1,\\
(X^\top X)_{33} &= 1\cdot1 + 0\cdot0 + 1\cdot1 = 2.
\end{aligned}
$$

Thus

$$
X^\top X
= \begin{pmatrix}
3 & 2 & 2\\
2 & 2 & 1\\
2 & 1 & 2
\end{pmatrix}.
$$

---

### Step 2: Compute $X^\top y$

Each entry is $\sum_{k=1}^3 X_{k,i}\,y_k$:

$$
\begin{aligned}
(X^\top y)_1 &= 1\cdot1 + 1\cdot2 + 1\cdot3 = 6,\\
(X^\top y)_2 &= 0\cdot1 + 1\cdot2 + 1\cdot3 = 5,\\
(X^\top y)_3 &= 1\cdot1 + 0\cdot2 + 1\cdot3 = 4.
\end{aligned}
$$

Hence

$$
X^\top y = \begin{pmatrix}6\\5\\4\end{pmatrix}.
$$

---

### Step 3: Invert $X^\top X$

1. **Determinant**  
   $$
   \det(X^\top X)
   = 3\begin{vmatrix}2&1\\1&2\end{vmatrix}
   - 2\begin{vmatrix}2&1\\2&2\end{vmatrix}
   + 2\begin{vmatrix}2&2\\2&1\end{vmatrix}
   = 3(4-1) - 2(4-2) + 2(2-4)
   = 9 - 4 - 4
   = 1.
   $$

2. **Cofactor matrix $C$**  
   $$
   C_{ij} = (-1)^{i+j}\det\bigl((X^\top X)_{\!-\{i\},-\{j\}}\bigr)
   \quad\Longrightarrow\quad
   C = \begin{pmatrix}
     3 & -2 & -2\\
    -2 &  2 &  1\\
    -2 &  1 &  2
   \end{pmatrix}.
   $$

3. **Adjugate = $C^\top$** (here symmetric)  
4. **Inverse**  
   $$
   (X^\top X)^{-1}
   = \frac{1}{\det(X^\top X)}\,\operatorname{adj}(X^\top X)
   = C^\top
   = \begin{pmatrix}
     3 & -2 & -2\\
    -2 &  2 &  1\\
    -2 &  1 &  2
   \end{pmatrix}.
   $$

---

### Step 4: Solve for $\hat\beta$

Multiply:

$$
\hat\beta
= (X^\top X)^{-1}\,X^\top y
= \begin{pmatrix}
 3 & -2 & -2\\
-2 &  2 &  1\\
-2 &  1 &  2
\end{pmatrix}
\begin{pmatrix}6\\5\\4\end{pmatrix}
=
\begin{pmatrix}
3\cdot6 +(-2)\cdot5 +(-2)\cdot4\\
(-2)\cdot6 + 2\cdot5 +1\cdot4\\
(-2)\cdot6 + 1\cdot5 +2\cdot4
\end{pmatrix}
=
\begin{pmatrix}0\\2\\1\end{pmatrix}.
$$

So $\hat\beta_0=0,\;\hat\beta_1=2,\;\hat\beta_2=1$, giving

$$
\hat y = 0 + 2\,x_1 + 1\,x_2,
$$

which exactly fits all three observations.