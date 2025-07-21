import matplotlib.pyplot as plt

def plot_iqr_outliers_with_boxplot(df, features=None, figsize=(14, 5), point_alpha=0.7, outlier_size=100):
    """
    Plots IQR-based outlier scatter plots with corresponding boxplots for each feature.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        features (list): Features to plot. If None, all columns are used.
        figsize (tuple): Size of each row's figure (width, height).
        point_alpha (float): Opacity of data points.
        outlier_size (int): Marker size for outliers.
    """
    if features is None:
        features = df.columns.tolist()

    n_plots = len(features)
    fig, axes = plt.subplots(n_plots, 2, figsize=(figsize[0], figsize[1] * n_plots))

    # Ensure axes is 2D array even when n_plots == 1
    if n_plots == 1:
        axes = [axes]

    for i, feature in enumerate(features):
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)][feature]

        iqr_padding = 0.1 * (upper_bound - lower_bound)

        # Add margin to ensure lines are visible
        y_min = min(df[feature].min(), lower_bound) - iqr_padding
        y_max = max(df[feature].max(), upper_bound) + iqr_padding

        # Scatter plot
        ax_scatter = axes[i][0] if n_plots > 1 else axes[0]
        ax_scatter.scatter(df.index, df[feature], color='blue', alpha=point_alpha, label='Data')

        if not outliers.empty:
            ax_scatter.scatter(outliers.index, outliers, color='red', edgecolors='black',
                            s=outlier_size, label='Outliers')

        ax_scatter.axhline(lower_bound, color='red', linestyle='dotted', linewidth=2,
                        label=f'Lower Bound: {lower_bound:.2f}')
        ax_scatter.axhline(upper_bound, color='brown', linestyle='dotted', linewidth=2,
                        label=f'Upper Bound: {upper_bound:.2f}')
        ax_scatter.set_ylim(y_min, y_max)
        ax_scatter.set_title(f'IQR Outlier Detection for {feature}')

        # Boxplot
        ax_box = axes[i][1] if n_plots > 1 else axes[1]
        ax_box.boxplot(df[feature].dropna(), vert=True, patch_artist=True,
                    boxprops=dict(facecolor='lightgray'),
                    whis=1.5)
        ax_box.set_ylim(y_min, y_max)
        ax_box.set_title(f'Boxplot for {feature}')

    plt.tight_layout()
    plt.show()