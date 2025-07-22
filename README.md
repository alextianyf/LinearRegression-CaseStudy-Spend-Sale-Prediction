# Linear Regression Case Study - Sales VS Advertising budget

> This is a Linear Regression portfolio project. Thus, this project focuses on <strong>Simple Linear Regression</strong> and its <strong>interpretability, foundational importance, and relevance in statistical learning</strong>. Even though it is necessary to discuss the best machine learning approach to solve this problem, this will not included in current stage, and may be discussed in the future work.

- Suppose that we are statistical consultants hired by a client to investigate the association between advertising and sales of a particular product.
- We are provided the dataset consists of the **sales** of one particular product in 200 diferent markets, along with advertising budgets for the product in each of those markets for three diferent media: **TV**, **Radio**, and **newspaper**.
- Client has **full control** of advertising expenses in each of the three media.
- If we determine that there is an association between advertising and alses, then we can instruct our client to adjust advertising budgets, thereby indirectly increasing sales.

# Objective

- This is designed as portfolio project, and mainly is designed to demonstrate the understanding of linear regression. We may not discuss the motivation of why using linear regression instead of other algorithms for this application.
- Our goal is to develop an accurate model that can be used to predict sales on the basis of the three media budgets.

# Important Questions that We Might Seek to Address

1. Is there a relationship between advertising budget and sales?
2. How strong is the relationship between advertising budget and sales?
3. Which media are associated with sales?
4. How large is the association between each medium and sales?
5. How accurately can we predict future sales?
6. Is the relationship linear?
7. Is there synergy among the advertising media?

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

To open a terminal in VS Code, use the shortcut: Ctrl + backtick ()

---

### 2. Active the Virtual Environment(On Windows, the activation command may differ)

Run the following command in your terminal:

```bash
source venv/bin/active
```

---

### 3. Select the Python Interpreter in VS Code

1. Press **`Cmd + Shift + P`** to open the Command Palette  
2. Search for: **`Python: Select Interpreter`**  
3. Choose the one that points to `./.venv`

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

This project uses the `Advertising.csv` dataset originally featured in the book:

**"An Introduction to Statistical Learning"** by Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani.  
The dataset is used here strictly for **educational and demonstration purposes**.

- All code in this repository is licensed under the [MIT License](./LICENSE).
- Notebooks and teaching materials are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), allowing you to remix, adapt, and build upon the material for any purpose, even commercially, **as long as credit is given to the original author** (Alex Tian).
- The original materials and resources can be found in [ISL Website](https://www.statlearning.com/resources-python)

> If you wish to use the dataset for commercial use beyond education, please refer to the book publisher’s terms and conditions.