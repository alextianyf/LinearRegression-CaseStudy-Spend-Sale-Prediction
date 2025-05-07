## 1. Why these concepts matter

- **Variance** quantifies how “spread out” your data are around their mean.  
- **Standard deviation** is the square root of variance, putting dispersion back into the original units.  
- **[Standard error](https://www.youtube.com/watch?v=A82brFpdr9g&list=LL&index=3)** tells you how much a sample statistic (like a sample mean) tends to vary from sample to sample.

---

## 2. Population vs. sample

| Quantity               | Population version                                     | Sample version                                                |
|------------------------|--------------------------------------------------------|---------------------------------------------------------------|
| Mean                   | $\displaystyle \mu = \frac{1}{N}\sum_{i=1}^N x_i$       | $\displaystyle \bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$          |
| Variance               | $\displaystyle \sigma^2 = \frac{1}{N}\sum_{i=1}^N (x_i - \mu)^2$ | $\displaystyle s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2$ |
| Standard deviation     | $\displaystyle \sigma = \sqrt{\sigma^2}$               | $\displaystyle s = \sqrt{s^2}$                                |
| Standard error of mean | $\displaystyle \frac{\sigma}{\sqrt{N}}$               | $\displaystyle \frac{s}{\sqrt{n}}$                            |

> **Why the $n-1$?**  
> When estimating variance from a sample, dividing by $n-1$ (Bessel’s correction) corrects for the fact that $\bar{x}$ is itself estimated.

---

## 3. Variance

**Definition**: The **sample variance** measures the average squared deviation from the mean.

$$
s^2 \;=\; \frac{1}{n - 1}
\sum_{i=1}^{n} \bigl(x_i - \bar{x}\bigr)^2.
$$

- **Units**: squared units of the original data (e.g. volts²).  
- **Intuition**: Squaring magnifies larger deviations, so outliers inflate the variance more.

---

## 4. Standard deviation

**Definition**: The **sample standard deviation** is the square root of the variance.

$$
s = \sqrt{s^2}
  = \sqrt{
    \frac{1}{n - 1}
    \sum_{i=1}^{n} (x_i - \bar{x})^2
  }.
$$

- **Units**: same as the original data (e.g. volts).  
- **Interpretation**:  
  - ≈68% of values lie within $\bar{x}\pm s$ for a normal distribution.  
  - ≈95% lie within $\bar{x}\pm2s$.

---

## 5. Standard error

**Definition**: The **standard error of the mean** quantifies how much $\bar{x}$ would vary across repeated samples.

$$
\mathrm{SE}_{\bar{x}}
=
\frac{s}{\sqrt{n}}.
$$

- **Units**: same as the original data.  
- **Intuition**: Larger $n$ → smaller SE → more precise mean estimate. SE shrinks at rate $1/\sqrt{n}$.  
- **Use in inference**:  
  - Confidence interval: $\displaystyle \bar{x}\pm t^*\,\mathrm{SE}_{\bar{x}}$  
  - Test statistic: $\displaystyle t = \frac{\bar{x}-\mu_0}{\mathrm{SE}_{\bar{x}}}$

---

## 6. Worked example

Sample of $n=5$ voltage readings (volts):
$$
x = [2.0,\;4.5,\;5.0,\;3.5,\;6.0].
$$

1. **Mean**:  
   $\displaystyle \bar{x} = \frac{2 + 4.5 + 5 + 3.5 + 6}{5} = 4.2.$

2. **Deviations**:  
   $x_i - \bar{x} = [-2.2,\;0.3,\;0.8,\;-0.7,\;1.8].$

3. **Squared deviations**:  
   $(x_i - \bar{x})^2 = [4.84,\;0.09,\;0.64,\;0.49,\;3.24].$

4. **Variance**:  
   $$
     s^2
     = \frac{1}{4}(4.84+0.09+0.64+0.49+3.24)
     = \frac{9.30}{4}
     = 2.325.
   $$

5. **Standard deviation**:  
   $$
     s = \sqrt{2.325}
       \approx 1.525\text{ V}.
   $$

6. **Standard error**:  
   $$
     \mathrm{SE}_{\bar{x}}
     = \frac{1.525}{\sqrt{5}}
     \approx 0.682\text{ V}.
   $$

> **Interpretation**: Individual readings vary by $\approx1.525$ V; the sample mean varies by $\approx0.682$ V across samples.

---

## 7. How they relate

1. Variance → SD: $s = \sqrt{s^2}$.  
2. SD → SE: $\mathrm{SE}_{\bar{x}} = \dfrac{s}{\sqrt{n}}$.  
3. Larger $n$ reduces SE by $1/\sqrt{n}$, improving precision.

---

## 8. Quick checklist

- **Variance** for dispersion in **squared units**.  
- **Standard deviation** for dispersion in **original units**.  
- **Standard error** for the **precision** of the sample mean.