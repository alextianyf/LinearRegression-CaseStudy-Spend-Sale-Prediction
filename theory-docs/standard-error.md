# Standard Error (SE)

The **Standard Error (SE)** measures **how much your estimate would vary** if you repeated the same experiment or sampling process over and over again.

Why is Standard Error Important?

- It tells you how precise your estimate is. A small SE means your estimate is stable and trustworthy.
- It’s used to build **confidence intervals**.
- It helps with hypothesis testing. You use SE to compute **t-values** and **p-values** to test if a coefficient is significantly different from 0.

---

## Standard Error for $\hat{\beta}_1$, ${SE}(\hat{\beta}_1)$

In a simple linear regression model, we have:

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad \varepsilon_i \sim \text{i.i.d. } N(0, \sigma^2)
$$

We aim to derive the **standard error** of the OLS estimator $\hat{\beta}_1$, which is:

$$
\text{SE}(\hat{\beta}_1) = \sqrt{\mathrm{Var}(\hat{\beta}_1)}
$$

**Step 1: Formula for $\beta_1$**

The OLS estimator for the slope $\beta_1$ is:

$$
\hat{\beta}_1 = \frac{ \sum (x_i - \bar{x})(y_i - \bar{y}) }{ \sum (x_i - \bar{x})^2 }
$$

We now substitute the model expression for $y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$.

To do this correctly, we also compute $\bar{y}$, the sample mean of all $y_i$'s:

$$
\bar{y} = \frac{1}{n} \sum y_i = \frac{1}{n} \sum \left( \beta_0 + \beta_1 x_i + \varepsilon_i \right)
= \beta_0 + \beta_1 \bar{x} + \bar{\varepsilon}
$$

Thus, the difference $y_i - \bar{y}$ becomes:

$$
y_i - \bar{y} = \left( \beta_0 + \beta_1 x_i + \varepsilon_i \right) - \left( \beta_0 + \beta_1 \bar{x} + \bar{\varepsilon} \right)
= \beta_1(x_i - \bar{x}) + \varepsilon_i - \bar{\varepsilon}
$$

Now plug the expression into the OLS formula:

$$
\hat{\beta}_1 = \frac{ \sum (x_i - \bar{x}) \left[ \beta_1(x_i - \bar{x}) + \varepsilon_i - \bar{\varepsilon} \right] }{ \sum (x_i - \bar{x})^2 }
$$

Expand the numerator using linearity of summation:

$$
\hat{\beta}_1 = \frac{\beta_1 \sum (x_i - \bar{x})^2 + \sum (x_i - \bar{x}) \varepsilon_i - \sum (x_i - \bar{x}) \bar{\varepsilon}}{\sum (x_i - \bar{x})^2}
$$

Note that $\sum (x_i - \bar{x}) = 0$, so:

$$
\sum (x_i - \bar{x}) \bar{\varepsilon} = \bar{\varepsilon} \cdot \sum (x_i - \bar{x}) = 0
$$

Thus the expression simplifies to:

$$
\hat{\beta}_1 = \beta_1 + \frac{ \sum (x_i - \bar{x}) \varepsilon_i }{ \sum (x_i - \bar{x})^2 }
$$

Let $S_{xx} = \sum (x_i - \bar{x})^2$, then:

$$
\hat{\beta}_1 = \beta_1 + \frac{ \sum a_i \varepsilon_i }{ S_{xx} },\quad\text{where } a_i = x_i - \bar{x}
$$

**Step 2: Compute the Variance of $\beta_1$**

$$
\mathrm{Var}(\hat{\beta}_1) = \mathrm{Var} \left( \frac{ \sum a_i \varepsilon_i }{ S_{xx} } \right)
= \frac{1}{S_{xx}^2} \cdot \mathrm{Var} \left( \sum a_i \varepsilon_i \right)
$$

Since $\varepsilon_i \sim \text{i.i.d.} \text{ and } \mathrm{Var}(\varepsilon_i) = \sigma^2\text{:}$:

$$
\operatorname{Var} \left( \sum a_i \varepsilon_i \right)
= \sum a_i^2 \cdot \operatorname{Var}(\varepsilon_i) = \sigma^2 \sum a_i^2 = \sigma^2 S_{xx}
$$

Then:

$$
\mathrm{Var}(\hat{\beta}_1) = \frac{ \sigma^2 S_{xx} }{ S_{xx}^2 } = \frac{ \sigma^2 }{ S_{xx} }
$$

**Step 3: Final Standard Error Formula**

$$
\text{SE}(\hat{\beta}_1) = \sqrt{ \frac{ \sigma^2 }{ \sum (x_i - \bar{x})^2 } }
$$

Since $\sigma^2$ is unknown in real-world data, we estimate it using Residual Standard Error, RSE:

$$
\boxed{
\hat{\sigma}^2 = \frac{1}{n - 2} \sum (y_i - \hat{y}_i)^2
}
$$

Therefore, the estimated standard error becomes:

$$
\boxed{
\text{SE}(\hat{\beta}_1) = \sqrt{ \frac{ \hat{\sigma}^2 }{ \sum (x_i - \bar{x})^2 } }
}
$$

---

## Standard Error for $\hat{\beta}_0$, ${SE}(\hat{\beta}_0)$

**Step 1: OLS Formula for $\beta_0$**

The OLS estimator for the intercept is:

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}
$$

This formula comes from rearranging the regression line to pass through the point $ (\bar{x}, \bar{y}) $, which is a property of the least squares line.

**Step 2: Compute the Variance of $\beta_0$**

We apply the variance formula for a linear combination of random variables:

$$
\mathrm{Var}(\hat{\beta}_0) = \mathrm{Var}(\bar{y} - \hat{\beta}_1 \bar{x})
$$

Since $\bar{x}$ is constant (it's computed from the observed values), we treat it as a scalar:

$$
= \mathrm{Var}(\bar{y}) + \bar{x}^2 \cdot \mathrm{Var}(\hat{\beta}_1)
- 2 \cdot \bar{x} \cdot \mathrm{Cov}(\bar{y}, \hat{\beta}_1)
$$

**Step 3: Evaluate Each Term**

1. Variance of $\bar{y}$

We know that the sample mean is defined as:

$$\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$$

From the regression model $y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$, we see that the randomness in $y_i$ comes from the error term $\varepsilon_i$. Since $\beta_0$, $\beta_1$, and $x_i$ are fixed values, the only random part of $\bar{y}$ is the average of the errors:

$$\bar{y} = \beta_0 + \beta_1 \bar{x} + \bar{\varepsilon}, \quad \text{where } \bar{\varepsilon} = \frac{1}{n} \sum_{i=1}^{n} \varepsilon_i$$

Therefore, the variance of $\bar{y}$ is equal to the variance of $\bar{\varepsilon}$. Because the $\varepsilon_i$’s are independent and identically distributed with variance $\sigma^2$, we use a standard result from probability:

$$
\mathrm{Var}(\bar{\varepsilon}) = \mathrm{Var} \left( \frac{1}{n} \sum_{i=1}^n \varepsilon_i \right)
= \frac{1}{n^2} \sum_{i=1}^n \mathrm{Var}(\varepsilon_i)
= \frac{1}{n^2} \cdot n \cdot \sigma^2
= \frac{\sigma^2}{n}
$$

So:

$$
\mathrm{Var}(\bar{y}) = \frac{\sigma^2}{n}
$$

2. Variance of $\hat{\beta}_1$

Previously derived as:

$$
\mathrm{Var}(\hat{\beta}_1) = \frac{\sigma^2}{\sum (x_i - \bar{x})^2}
$$

Let $S_{xx} = \sum (x_i - \bar{x})^2$

3. Covariance Term

Under the assumption that $\varepsilon_i$ are i.i.d. and independent of $x_i$, it can be shown that:

$$
\mathrm{Cov}(\bar{y}, \hat{\beta}_1) = 0
$$


**Step 4: Combine the Results**

$$
\operatorname{Var}(\hat{\beta}_0)
= \frac{\sigma^2}{n} + \bar{x}^2 \cdot \frac{\sigma^2}{S_{xx}}
= \sigma^2 \left( \frac{1}{n} + \frac{\bar{x}^2}{S_{xx}} \right)
$$

**Step 5: Final Standard Error Formula**

$$
\boxed{
\text{SE}(\hat{\beta}_0) = \sqrt{ \sigma^2 \left( \frac{1}{n} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2} \right) }
}
$$

Since $\sigma^2$ is unknown in practice, it is estimated by:

$$
\hat{\sigma}^2 = \frac{1}{n - 2} \sum (y_i - \hat{y}_i)^2
$$

Therefore, the estimated standard error is:

$$
\boxed{
\text{SE}(\hat{\beta}_0) = \sqrt{ \hat{\sigma}^2 \left( \frac{1}{n} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2} \right) }
}
$$