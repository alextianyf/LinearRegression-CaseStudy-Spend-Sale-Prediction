import matplotlib.pyplot as plt

def plot_iqr_outliers(df, features=None, n_cols=4, figsize=(16, 5), point_alpha=0.7, outlier_size=100):
    """
    Plots scatter plots for specified features with IQR outlier detection and annotated legend.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        features (list): Features to plot. If None, all columns are used.
        n_cols (int): Number of columns in the subplot grid.
        figsize (tuple): Size of the overall figure.
        point_alpha (float): Opacity of data points.
        outlier_size (int): Marker size for outliers.
    """
    if features is None:
        features = df.columns.tolist()

    n_plots = len(features)
    n_rows = (n_plots + n_cols - 1) // n_cols

    plt.figure(figsize=figsize)

    for i, feature in enumerate(features):
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)][feature]

        plt.subplot(n_rows, n_cols, i + 1)
        plt.scatter(df.index, df[feature], color='blue', alpha=point_alpha, label='Data')

        if not outliers.empty:
            plt.scatter(outliers.index, outliers, color='red', edgecolors='black', s=outlier_size, label='Outliers')

        plt.axhline(lower_bound, color='purple', linestyle='dotted', linewidth=2,
                    label=f'Lower Bound: {lower_bound:.2f}')
        plt.axhline(upper_bound, color='brown', linestyle='dotted', linewidth=2,
                    label=f'Upper Bound: {upper_bound:.2f}')

        plt.xlabel("Index")
        plt.ylabel(feature)
        plt.title(f"{feature} (IQR Outliers)")
        plt.legend(loc='best', fontsize=8)

    plt.tight_layout()
    plt.show()