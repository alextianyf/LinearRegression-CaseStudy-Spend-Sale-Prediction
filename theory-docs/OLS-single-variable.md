# Manual Calculation of OLS Coefficients

The following calculations are based on the [Ordinary Least Squares (OLS)](https://en.wikipedia.org/wiki/Ordinary_least_squares) method. We are modeling the relationship between variables X and Y using:

$$\hat{y}_i = \beta_0 + \beta_1 x_i$$

We want to find the best $\beta_0$ (intercept) and $\beta_1$ (slope) such that the sum of squared errors (SSE) is minimized The Cost Function:

$$S(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - \hat{y}i)^2 = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$$

**Partial Derivative with respect to $\beta_0$:**

$$\frac{\partial S}{\partial \beta_0} = -2 \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i) = 0$$

$$n \beta_0 + \beta_1 \sum x_i = \sum y_i$$

$$
\text{Where } n\bar{x} = \sum x_i \quad \text{and} \quad n\bar{y} = \sum y_i
$$

$${n}\beta_0 = {n}\bar{y} - {n}\beta_1 \bar{x}$$

$$
\boxed{
\beta_0 = \bar{y} - \beta_1 \bar{x}
}
$$

$$\beta_0 = \bar{y} - \beta_1 \bar{x} \quad \text{→ Equation (1)}$$

**Partial Derivative with respect to $\beta_1$:**

$$\frac{\partial S}{\partial \beta_1} = -2 \sum_{i=1}^{n} x_i (y_i - \beta_0 - \beta_1 x_i) = 0$$

$$\sum x_i y_i - \beta_0 \sum x_i - \beta_1 \sum x_i^2 = 0 \quad \text{→ Equation (2)}$$

Now, substitute **Equation (1)** $(\beta_0 = \bar{y} - \beta_1 \bar{x})$ into **Equation (2)**.

$$\sum x_i y_i - \bar{y} \sum x_i + \beta_1 \bar{x} \sum x_i - \beta_1 \sum x_i^2 = 0$$

$$\sum x_i y_i - \bar{y} \sum x_i + \beta_1 \left( \bar{x} \sum x_i - \sum x_i^2 \right) = 0$$

$$\sum x_i y_i - n \bar{x} \bar{y} + \beta_1 \left( n \bar{x}^2 - \sum x_i^2 \right) = 0$$

$$\beta_1 \left( n \bar{x}^2 - \sum x_i^2 \right) = n \bar{x} \bar{y} - \sum x_i y_i$$

Multiply both sides by -1 to get positive denominators:

$$\beta_1 \left( \sum x_i^2 - n \bar{x}^2 \right) = \sum x_i y_i - n \bar{x} \bar{y}$$

$$
\boxed{
\beta_1 = \frac{\sum x_i y_i - n \bar{x} \bar{y}}{\sum x_i^2 - n \bar{x}^2}
}
$$

$$\sum (x_i - \bar{x})(y_i - \bar{y}) = \sum x_i y_i - \bar{y} \sum x_i - \bar{x} \sum y_i + n \bar{x} \bar{y}$$

$$\sum (x_i - \bar{x})(y_i - \bar{y})
= \sum x_i y_i - \bar{y} (n \bar{x}) - \bar{x} (n \bar{y}) + n \bar{x} \bar{y}
= \sum x_i y_i - n \bar{x} \bar{y} - n \bar{x} \bar{y} + n \bar{x} \bar{y}
= \sum x_i y_i - n \bar{x} \bar{y}$$

$$\sum (x_i - \bar{x})^2
= \sum x_i^2 - 2\bar{x} \sum x_i + n \bar{x}^2
= \sum x_i^2 - 2\bar{x} (n \bar{x}) + n \bar{x}^2
= \sum x_i^2 - 2n \bar{x}^2 + n \bar{x}^2
= \sum x_i^2 - n \bar{x}^2
$$

This is also equivalent to:

$$
\boxed{
\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
}
$$

**Final OLS Estimators:**

$$
\boxed{\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}}
\quad , \quad
\boxed{\beta_0 = \bar{y} - \beta_1 \bar{x}}
$$