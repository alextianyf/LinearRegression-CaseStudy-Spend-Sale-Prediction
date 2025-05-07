# Standard Error (SE)

The **Standard Error (SE)** measures **how much your estimate would vary** if you repeated the same experiment or sampling process over and over again.

**Why is Standard Error Important?**

- It tells you how precise your estimate is. A small SE means your estimate is stable and trustworthy.  
- It’s used to build **confidence intervals**.  
- It helps with hypothesis testing: you use SE to compute **t-values** and **p-values** to test if a coefficient is significantly different from 0.

---

## Standard Error for \(\hat{\beta}_1\) \(\bigl(\mathrm{SE}(\hat{\beta}_1)\bigr)\)

In a simple linear regression model, we have:

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i,\quad
\varepsilon_i \sim \text{i.i.d. }N(0, \sigma^2).
$$

We aim to derive the **standard error** of the OLS estimator \(\hat{\beta}_1\), which is

$$
\mathrm{SE}(\hat{\beta}_1) = \sqrt{\mathrm{Var}(\hat{\beta}_1)}.
$$

### Step 1: Formula for \(\hat{\beta}_1\)

The OLS estimator for the slope is

$$
\hat{\beta}_1
= \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}
       {\sum (x_i - \bar{x})^2}.
$$

Substitute \(y_i = \beta_0 + \beta_1 x_i + \varepsilon_i\).  First note

$$
\bar{y}
= \frac{1}{n}\sum_{i=1}^n y_i
= \beta_0 + \beta_1\bar{x} + \bar{\varepsilon},
$$

so

$$
y_i - \bar{y}
= \beta_1(x_i - \bar{x}) + (\varepsilon_i - \bar{\varepsilon}).
$$

Plugging in,

$$
\hat{\beta}_1
= \frac{\sum (x_i - \bar{x})\bigl[\beta_1(x_i - \bar{x}) + (\varepsilon_i - \bar{\varepsilon})\bigr]}
       {\sum (x_i - \bar{x})^2}
= \beta_1 + \frac{\sum (x_i - \bar{x})\,\varepsilon_i}{\sum (x_i - \bar{x})^2},
$$

since \(\sum (x_i-\bar{x})=0\).  Let

$$
S_{xx} = \sum (x_i - \bar{x})^2,\quad
a_i = x_i - \bar{x},
$$

then

$$
\hat{\beta}_1 = \beta_1 + \frac{\sum a_i\,\varepsilon_i}{S_{xx}}.
$$

### Step 2: Variance of \(\hat{\beta}_1\)

$$
\mathrm{Var}(\hat{\beta}_1)
= \mathrm{Var}\Bigl(\tfrac{\sum a_i\varepsilon_i}{S_{xx}}\Bigr)
= \frac{1}{S_{xx}^2}\,\mathrm{Var}\Bigl(\sum a_i\varepsilon_i\Bigr)
= \frac{1}{S_{xx}^2}\,\bigl(\sigma^2\sum a_i^2\bigr)
= \frac{\sigma^2}{S_{xx}}.
$$

So

$$
\mathrm{SE}(\hat{\beta}_1)
= \sqrt{\frac{\sigma^2}{\sum (x_i - \bar{x})^2}}.
$$

In practice \(\sigma^2\) is unknown and estimated by
\(\;\hat\sigma^2=\tfrac{1}{n-2}\sum(y_i-\hat y_i)^2\;\), giving

$$
\boxed{
\mathrm{SE}(\hat{\beta}_1)
= \sqrt{\frac{\hat\sigma^2}{\sum (x_i - \bar{x})^2}}.
}
$$

---

## Standard Error for \(\hat{\beta}_0\) \(\bigl(\mathrm{SE}(\hat{\beta}_0)\bigr)\)

### Step 1: Formula for \(\hat{\beta}_0\)

The intercept estimator is

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}.
$$

### Step 2: Variance of \(\hat{\beta}_0\)

By linear‐combination rules,

$$
\mathrm{Var}(\hat{\beta}_0)
= \mathrm{Var}(\bar{y} - \bar{x}\,\hat{\beta}_1)
= \mathrm{Var}(\bar{y})
+ \bar{x}^2\,\mathrm{Var}(\hat{\beta}_1)
-2\bar{x}\,\mathrm{Cov}(\bar{y},\hat{\beta}_1).
$$

One can show \(\mathrm{Cov}(\bar{y},\hat{\beta}_1)=0\).  Also

$$
\mathrm{Var}(\bar{y})=\frac{\sigma^2}{n},\quad
\mathrm{Var}(\hat{\beta}_1)=\frac{\sigma^2}{S_{xx}}.
$$

Hence

$$
\mathrm{Var}(\hat{\beta}_0)
= \sigma^2\Bigl(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\Bigr),
$$

so

$$
\mathrm{SE}(\hat{\beta}_0)
= \sqrt{\sigma^2\Bigl(\frac{1}{n} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2}\Bigr)}.
$$

Replacing with \(\hat\sigma^2\) gives

$$
\boxed{
\mathrm{SE}(\hat{\beta}_0)
= \sqrt{\hat\sigma^2\Bigl(\frac{1}{n} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2}\Bigr)}.
}
$$