import statsmodels.api as sm

def forward_selection(data, response, significance_level=0.05, candidate_order=None, verbose=True):
    """
    Forward selection with detailed logging of each variable evaluation.

    Parameters:
    -----------
    data : DataFrame
        Input data including predictors and response.
    response : str
        Name of the response variable.
    significance_level : float
        Threshold for p-value to include variable.
    candidate_order : list or None
        Optional list of predictor names to specify the order of evaluation.
    verbose : bool
        Whether to print logs for each step.

    Returns:
    --------
    selected_vars : list
        List of selected variables in order.
    final_model : RegressionResults
        Fitted statsmodels OLS model.
    """
    all_vars = list(data.columns)
    all_vars.remove(response)

    # Use custom candidate order if given
    if candidate_order is not None:
        remaining_vars = [var for var in candidate_order if var in all_vars]
    else:
        remaining_vars = all_vars.copy()

    selected_vars = []
    step = 1

    while remaining_vars:
        best_candidate = None
        best_pval = None
        best_rss = None
        best_model = None

        if verbose:
            print(f"\nStep {step} | Current model: {selected_vars}")

        for candidate in remaining_vars:
            model = sm.OLS(data[response], sm.add_constant(data[selected_vars + [candidate]])).fit()
            pval = model.pvalues[candidate]
            rss = ((model.resid) ** 2).sum()

            if verbose:
                print(f"   → Evaluating '{candidate}': p-value = {pval:.4f} | RSS = {rss:.4f}")

            if best_pval is None or pval < best_pval:
                best_candidate = candidate
                best_pval = pval
                best_rss = rss
                best_model = model

        if best_pval < significance_level:
            selected_vars.append(best_candidate)
            remaining_vars.remove(best_candidate)
            if verbose:
                print(f"Added: {best_candidate} (p = {best_pval:.4f} < {significance_level})")
        else:
            if verbose:
                print("No variable meets the significance threshold. Stopping.")
            break

        step += 1

    final_model = sm.OLS(data[response], sm.add_constant(data[selected_vars])).fit()
    return selected_vars, final_model

def backward_selection(data, response, significance_level=0.05, verbose=True):
    """
    Perform backward selection by evaluating each variable's p-value at each step,
    printing p-value, RSS, and decision for each variable.

    Parameters:
    -----------
    data : DataFrame
        Dataset including predictors and response.
    response : str
        Name of the response variable.
    significance_level : float
        Threshold for maximum p-value to keep a variable.
    verbose : bool
        Whether to print step-by-step logs.

    Returns:
    --------
    selected_vars : list
        Final list of variables kept in the model.
    final_model : RegressionResults
        statsmodels OLS model with selected variables.
    """
    selected_vars = list(data.columns)
    selected_vars.remove(response)

    step = 1
    while True:
        model = sm.OLS(data[response], sm.add_constant(data[selected_vars])).fit()
        pvalues = model.pvalues.drop('const')
        rss = ((model.resid) ** 2).sum()

        if verbose:
            print(f"\nStep {step} | Current model: {selected_vars}")
            print("P-values and RSS:")

            for var in selected_vars:
                print(f"   - {var}: p-value = {pvalues[var]:.4f}")

            print(f"   RSS = {rss:.4f}")

        # Check if any variable has p > threshold
        max_pval = pvalues.max()
        if max_pval > significance_level:
            worst_var = pvalues.idxmax()
            if verbose:
                print(f"Removing '{worst_var}' (p = {max_pval:.4f} > {significance_level})")
            selected_vars.remove(worst_var)
            step += 1
        else:
            if verbose:
                print("All variables have p-values below threshold. Stopping.")
            break

    final_model = sm.OLS(data[response], sm.add_constant(data[selected_vars])).fit()
    return selected_vars, final_model