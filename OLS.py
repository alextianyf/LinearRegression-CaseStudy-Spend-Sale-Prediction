def Simple_OLS(df, feature, predict):
    """
    Manually compute OLS coefficients (intercept and slope)
    for simple linear regression.

    Parameters:
    - df (pd.DataFrame): The input dataframe.
    - feature (str): The name of the independent variable (X).
    - predict (str): The name of the dependent variable (y).

    Returns:
    - B0_Intercept (float): Intercept of the regression line.
    - B1_slope (float): Slope (coefficient for the feature).
    """
    X = df[feature]
    y = df[predict]

    x_mean = X.mean()
    y_mean = y.mean()

    # Intermediate steps for the OLS slope and intercept
    x_diff = X - x_mean
    y_diff = y - y_mean

    numerator = (x_diff * y_diff).sum()
    denominator = (x_diff ** 2).sum()

    B1_slope = numerator / denominator
    B0_Intercept = y_mean - B1_slope * x_mean

    return B0_Intercept, B1_slope