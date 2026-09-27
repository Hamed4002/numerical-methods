# Numerical Methods in Python

Numerical analysis algorithms implemented in Python, written for a university **Numerical Analysis** course. This repository covers interpolation, curve fitting, splines, numerical integration, and numerical differentiation.

## About

These implementations were built while studying numerical methods for the first time, using [SymPy](https://www.sympy.org/) for symbolic computation (solving equations, differentiation, polynomial expansion). Most scripts are interactive: they prompt for the number of data points and their values, then compute and print the result.

## Structure

```
numerical-methods-python/
├── interpolation/
│   ├── lagrange_interpolation.py
│   ├── newton_interpolation_symbolic.py
│   ├── newton_forward_equal_spacing.py
│   ├── newton_forward_divided_diff.py
│   ├── newton_backward_equal_spacing.py
│   └── newton_backward_divided_diff.py
├── splines/
│   ├── cubic_spline_simple.py
│   └── cubic_spline_general.py
├── curve_fitting/
│   └── least_squares_curve_fit.py
├── integration/
│   ├── trapezoidal_rule.py
│   ├── midpoint_rule_integration.py
│   ├── simpson_1_3_rule.py
│   ├── simpson_3_8_rule.py
│   └── newton_cotes_weights.py
└── differentiation/
    ├── numerical_derivative_simple.py
    └── numerical_derivative_symbolic.py
```

## Topics covered

- **Interpolation**: Lagrange's method, and Newton's method in several forms (symbolic/derivative-based, forward/backward with equally spaced points, and forward/backward using divided differences for unequally spaced points)
- **Splines**: cubic spline interpolation, a fixed-example version and a general version that takes any set of points
- **Curve fitting**: least-squares polynomial fitting of a given degree
- **Numerical integration**: trapezoidal rule, midpoint rule, Simpson's 1/3 and 3/8 rules, and Newton-Cotes quadrature weights
- **Numerical differentiation**: estimating derivatives from tabulated data using finite differences

## Requirements

```
pip install sympy
```
