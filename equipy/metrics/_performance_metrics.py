from sklearn.metrics import mean_squared_error
from utils.checkers import _check_metric

def performance(y_true, y_predict, metric=mean_squared_error):
    """
    Compute the performance value for predicted fair output compared to the true labels.

    Parameters:
    y_true (array-like): True labels or ground truth values.
    y_predict (array-like): Predicted (fair or not) output values.
    metric (function, optional): The metric used to compute the performance, default=sklearn.metrics.mean_square_error

    Returns:
    float: The calculated performance value.

    Example:
    >>> y_true = np.array([1, 0, 1, 1, 0])
    >>> y_predict = np.array([0, 1, 1, 1, 0])
    >>> classification_performance = performance(y_true, y_predict)
    >>> print(classification_performance)
    0.6

    >>> y_true = [1.2, 2.5, 3.8, 4.0, 5.2]
    >>> y_predict = [1.0, 2.7, 3.5, 4.2, 5.0]
    >>> regression_performance = performance(y_true, y_predict)
    >>> print(regression_performance)
    0.05
    """

    _check_metric(y_true)
    
    return metric(y_true, y_predict)

def performance_dict(y_true, y_fair_dict, metric=mean_squared_error):
    """
    Compute the performance values for multiple fair output datasets compared to the true labels.

    Parameters:
    y_true (array-like): True labels or ground truth values.
    y_fair_dict (dict): A dictionary containing sequentally fair output datasets.
    metric (function, optional): The metric used to compute the performance, default=sklearn.metrics.mean_square_error

    Returns:
    dict: A dictionary containing performance values for sequentally fair output datasets.

    Example:
    >>> y_true = np.array([15, 38, 68])
    >>> y_fair_dict = {'Base model':np.array([19,39,65]), 'sens_var_1':np.array([22,40,50]), 'sens_var_2':np.array([28,39,42])}
    >>> performance_values = performance_dict(y_true, y_fair_dict)
    >>> print(performance_values)
    {'Base model': 8.666666666666666, 'sens_var_1': 125.66666666666667, 'sens_var_2': 282.0}
    """
    performance_dict = {}
    for key in y_fair_dict.keys():
        performance_dict[key] = metric(y_true, list(y_fair_dict[key]))
    return performance_dict