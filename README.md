# Linear Regression Case Study – Sales vs. Advertising Budget

This portfolio project provides a comprehensive introduction to **Linear Regression** through hands-on case studies. It is structured in two major parts:

- **Simple Linear Regression**: Develop a model to predict **Sales** based solely on **TV advertising budget**.
- **Multiple Linear Regression**: Extend the model to predict **Sales** using **TV**, **Radio**, and **Newspaper** advertising budgets.

<div align="center">
  <img src="images/SLR.png" alt="Simple Linear Regression" height="300"/>
  <img src="images/MLR.png" alt="Multiple Linear Regression" height="300"/>
</div>

This project is designed as a **beginner-friendly starting point** for those looking to step into the world of **Machine Learning**. It also serves as a solid foundation for anyone who wants a **deep understanding of linear regression**, especially focusing on the following core concepts:

- Ordinary Least Squares (OLS)
- Gradient Descent
- Hypothesis Testing
- Manual Derivations & Explanations (not just library-based modeling)
- And other concepts...

Rather than relying heavily on pre-built libraries, this project emphasizes **manual implementation** and **theoretical insight**, helping you build true intuition about how linear regression works.

**NOTES:**

[1] This project emphasizes the **interpretability**, **theoretical foundation**, and **statistical learning relevance** of linear regression.  
[2] While real-world machine learning problems may call for alternative models, **this project focuses exclusively on linear regression** to maintain clarity and depth.  
[3] Advanced topics such as **regularization techniques** (e.g., Lasso), **train-test splits**, and other topics are intentionally excluded to preserve focus on core regression concepts.

---

## Table of Contents

- [Linear Regression Case Study – Sales vs. Advertising Budget](#linear-regression-case-study--sales-vs-advertising-budget)
  - [Table of Contents](#table-of-contents)
  - [Project Background](#project-background)
  - [Project Objective](#project-objective)
    - [Part 1: Simple Linear Regression - Sales vs. TV Advertising Budget](#part-1-simple-linear-regression---sales-vs-tv-advertising-budget)
    - [Part 2: Multiple Linear Regression](#part-2-multiple-linear-regression)
  - [File Structure](#file-structure)
  - [Development Environment Setup (with Virtual Environment)](#development-environment-setup-with-virtual-environment)
    - [Recommended Configuration](#recommended-configuration)
    - [1. Creating Virtual Environment](#1-creating-virtual-environment)
    - [2. Active the Virtual Environment(On Windows, the activation command may differ)](#2-active-the-virtual-environmenton-windows-the-activation-command-may-differ)
    - [3. Select the Python Interpreter in VS Code](#3-select-the-python-interpreter-in-vs-code)
    - [4. Install `ipykernel` (Recommended Version: 6.29.5)](#4-install-ipykernel-recommended-version-6295)
    - [5. Install Project Dependencies](#5-install-project-dependencies)
  - [Attribution \& Licensing](#attribution--licensing)

---

## Project Background

- Suppose we are statistical consultants hired by a client to investigate the relationship between advertising and product sales.
- We are provided with a dataset containing the **sales** of a particular product in **200 different markets**, along with the **advertising budgets** for three different media channels: **TV**, **Radio**, and **Newspaper**.
  - In the **Simple Linear Regression** case study, we analyze the relationship between **Sales** and **TV advertising** only.
  - In the **Multiple Linear Regression** case study, we explore how **Sales** relate to **TV**, **Radio**, and **Newspaper** advertising budgets.
- The client has **full control** over the advertising expenditures across all three media.
- If we find a significant association between advertising and sales, we can advise the client on how to **reallocate or optimize their ad budget** to potentially boost sales.

---

## Project Objective

This section outlines the key learning objectives and concepts you will explore throughout each part of the project. It serves as a roadmap for what you'll gain by completing the Simple and Multiple Linear Regression case studies.

### Part 1: Simple Linear Regression - Sales vs. TV Advertising Budget

> This phase focuses on building a solid foundation in both **data science tools** and **core statistical concepts** through the use case of predicting **Sales** based on **TV advertising budget**. The core topics covered are listed as following

- **Fundamental Python Libraries**:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, and `scipy`

- **Data Loading & Manipulation**:
  - Reading data into DataFrames
  - Conditional filtering
  - Dropping rows or columns
  - Data dropping

- **Data Visualization**:
  - Creating scatterplots and histograms
  - Interpreting scatterplot and histograms
  - Understanding different binning strategies:
    - **Freedman–Diaconis rule**
    - Other commonly used rules

- **Descriptive Statistics**:
  - Mean, median, mode, min, max, standard deviation
  - 25th and 75th percentiles (quartiles)
  - Connecting descriptive stats with visual insights

- **Noise and Outliers**:
  - Why noise negatively affects models
  - Using **IQR (Interquartile Range)** to detect and reduce noise

- **Correlation Analysis**:
  - Measuring correlation between **TV ad spend** and **Sales**
  - Interpreting correlation coefficients

- Develop an accurate model by understanding **Residual Sum of Squares (RSS)** Optimization:
  - Manually compute OLS (Ordinary Least Squares) solution
  - Implement Gradient Descent from scratch to estimate coefficients
  - Compare results from:
    - Manual OLS
    - Gradient Descent
    - Built-in tools (`numpy`, `scikit-learn`)
  - Discuss pros and cons of OLS vs. Gradient Descent
  - Interpret the best-fitting coefficient in a business context

- **Hypothesis Testing**:
  - Understanding **t-statistic** and **p-value**
  - Using p-value to support or reject the null hypothesis
  - Interpreting coefficient outputs: Standard Error, t-value, p-value

- **Confidence Intervals**:
  - Building 95% confidence intervals for coefficients
  - Interpreting CI bounds and model reliability

- **Performance Metrics**:
  - **Residual Standard Error (RSE)**
  - **R² (Coefficient of Determination)**
  - Interpret what these values mean for model accuracy and predictive power

- Based on model findings, we will explore and answer key business questions:
  - **Q1**: How does TV advertising affect product sales?
  - **Q2**: Can we quantify the return on every additional dollar spent on TV?
  - **Q3**: Is the relationship between TV spend and sales statistically significant?
  - **Q4**: How accurate is our model in predicting future sales?
  - **Q5**: To what extent can we rely on TV advertising alone for sales forecasting?
  - **Q6**: What is the expected sales level if no advertising budget is allocated?

- Discuss **model limitations** based on findings

- Provide **strategic business recommendations** derived from the analysis

---

### Part 2: Multiple Linear Regression

> This section expands the analysis to include **TV**, **Radio**, and **Newspaper** as predictors of Sales.

- Develop an accurate model to predict **Sales** using all three media budgets: **TV**, **Radio**, and **Newspaper**.
  - Manually derive the OLS solution using **linear algebra for multivariable regression**.
  - Compare results with the built-in implementation from **scikit-learn**.

- **Why Multiple Regression?**
  - Use the **correlation matrix** to understand why separate simple regressions may be misleading.
  - Justify the need for multivariable modeling to account for interaction and shared variance.

- **Variable Selection & Hypothesis Testing**:
  - Perform **F-statistic testing** to evaluate overall model significance.
  - Use **p-values**, **forward selection**, and **backward elimination** to identify important predictors.

- **Model Evaluation**:
  - Assess model performance using:
    - **Residual Standard Error (RSE)**
    - **R² (Coefficient of Determination)**

- **Prediction & Inference**:
  - Make predictions using both:
    - **Confidence Intervals (CI)** – for estimating the mean response
    - **Prediction Intervals (PI)** – for forecasting individual outcomes
  - Interpret the differences between CI and PI in context.

- **Interaction Effects (Synergy)**:
  - Explore whether combinations of media (e.g., TV + Radio) have an **amplified effect** on sales.
  - Investigate interaction terms in the regression model.

- **Model Diagnostics**:
  - Check for **linearity assumption** using residual plots and diagnostic tools.

- Based on the findings, we aim to answer:
  - **Q1**: **Is there a relationship** between sales and advertising budget?
  - **Q2**: **Which media** are significantly associated with sales?
  - **Q3**: **How strong** is the relationship?
  - **Q4**: **How large** is the association between each medium and sales?
  - **Q5**: **Is there synergy** among the advertising media?
  - **Q6**: **Is the relationship linear?**

---

## File Structure

This section provides a detailed overview of the project directory structure, helping you understand where key files and resources are located.

```text
.
├── .venv/                                # (Not included) Virtual environment folder
├── data/
│   ├── Advertising_simple.csv            # Dataset for Simple Linear Regression
│   └── Advertising.csv                   # Dataset for Multiple Linear Regression
├── images/                               # Conceptual illustrations and plots (exported from notebooks)
├── notebooks/                            # Main exploratory and explanatory Jupyter Notebooks
│   ├── 01-Simple-LinearRegression.ipynb
│   └── 02-Multiple-LinearRegression.ipynb
├── spend_sale_lib/                       # Custom Python module for reusable components
│   ├── feature-selection.py              # Manually implemented forward & backward selection
│   ├── Gradient_Descend.py               # Manual implementation of Gradient Descent algorithm
│   ├── IQR.py                            # IQR-based denoising helper
│   └── OLS.py                            # Manual implementation of OLS (Ordinary Least Squares)
├── theory-docs/                          # Supplementary theoretical documents and derivations
│   ├── 01-OLS-single-variable.md         # Mathematical proof for single-variable OLS
│   ├── 02-variance-stddev-stderr.md      # Concepts: Variance, Standard Deviation, Standard Error
│   ├── 03-SE-single-variable.ipynb       # Step-by-step derivation of Standard Error (single variable)
│   └── 04-OLS-MLR.ipynb                  # OLS derivation for Multiple Linear Regression
├── LICENSE                               # MIT License
├── README.md                             # Project overview (you are here)
└── requirements.txt                      # Required Python packages to run the project
```

## Development Environment Setup (with Virtual Environment)

> Note: These instructions are for macOS. Setup may differ slightly on Windows.

### Recommended Configuration

- Operating System: MacOS

- Recommended Python Version: 3.12.4

- Integrated Development Environment: Visual Studio Code (VS Code)

---

### 1. Creating Virtual Environment

Open your terminal in the project root directory and run:

```bash
python3 -m venv .venv
```

> It’s common practice to name the environment .venv. Most certainly, you could rename it accordingly.

To open a terminal in VS Code, use the shortcut: Ctrl + backtick (`)

---

### 2. Active the Virtual Environment(On Windows, the activation command may differ)

Run the following command in your terminal:

```bash
source .venv/bin/activate
```

---

### 3. Select the Python Interpreter in VS Code

Step 1: Press **`Cmd + Shift + P`** to open the Command Palette  

Step 2: Search for: **`Python: Select Interpreter`**  

Step 3: Choose the one that points to `./.venv`

---

### 4. Install `ipykernel` (Recommended Version: 6.29.5)

```bash
pip install ipykernel==6.29.5
```

> To verify or check your ipykernel installation version: `pip show ipykernel`

---

### 5. Install Project Dependencies

Install all required packages from the `requirements.txt`:

```bash
pip install -r requirements.txt
```

> You can modify or create your own environment by `pip freeze > requirements.txt`  
> you can use command `pip list` to list all installed packages

---

## Attribution & Licensing

This project uses the `Advertising_simple.csv` and `Advertising.csv` dataset originally featured in the book:

**"An Introduction to Statistical Learning"** by Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani.  
The dataset is used here strictly for **educational and demonstration purposes**.

- All code in this repository is licensed under the [MIT License](./LICENSE).
- Notebooks and teaching materials are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), allowing you to remix, adapt, and build upon the material for any purpose, even commercially, **as long as credit is given to the original author** (Alex Tian).
- The original materials and resources can be found in [ISL Website](https://www.statlearning.com/resources-python)

> If you wish to use the dataset for commercial use beyond education, please refer to the book publisher’s terms and conditions.
