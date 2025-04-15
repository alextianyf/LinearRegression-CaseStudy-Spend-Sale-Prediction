import numpy as np
import matplotlib.pyplot as plt

def simple_gradient_descent(df, target='Sales', feature=None,alpha=0.00001, epochs=300000,init_B0=0, init_B1=0, plot=True):
    """
    Perform simple linear regression using batch gradient descent on one or all features.

    Parameters:
    - df (pd.DataFrame): Dataset containing features and target.
    - target (str): Name of the target column.
    - feature (str or None): Feature name to run regression on. If None, use all except target.
    - alpha (float): Learning rate.
    - epochs (int): Number of gradient descent iterations.
    - init_B0 (float): Initial intercept value.
    - init_B1 (float): Initial slope value.
    - plot (bool): Whether to show the cost convergence plot.

    Returns:
    - results (dict): Contains B0, B1, and cost_history for each feature.
    """
    if feature is not None:
        features = [feature]
    else:
        features = [col for col in df.columns if col != target]

    y = df[target].values
    n = len(y)
    results = {}

    for feature in features:
        X_raw = df[feature].values
        X = (X_raw - np.mean(X_raw)) / np.std(X_raw)  # Standardize

        B0, B1 = init_B0, init_B1
        cost_history = []

        for _ in range(epochs):
            y_pred = B0 + B1 * X
            error = y - y_pred

            dB0 = -2 * np.sum(error) / n
            dB1 = -2 * np.sum(error * X) / n

            B0 -= alpha * dB0
            B1 -= alpha * dB1

            cost = np.mean(error ** 2)
            cost_history.append(cost)

        # Convert back to original scale
        B1_original = B1 / np.std(X_raw)
        B0_original = B0 - B1_original * np.mean(X_raw)

        results[feature] = {
            'B0': B0_original,
            'B1': B1_original,
            'cost_history': cost_history
        }

        print(f"\nFeature: {feature}")
        print(f"  Optimized B0 (Intercept): {B0_original:.4f}")
        print(f"  Optimized B1 (Slope):     {B1_original:.4f}")

    # Plot cost history
    if plot:
        plt.figure(figsize=(10, 6))
        for feature in features:
            plt.plot(results[feature]['cost_history'], label=feature)
        plt.xlabel("Iterations")
        plt.ylabel("Cost (MSE)")
        plt.title("Gradient Descent Convergence")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    return results