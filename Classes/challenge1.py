import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define an expression
expr = x**2 + y**2

# Print the expression
print("Expression:", expr)

# Expand the expression
expanded_expr = sp.expand(expr)
print("Expanded Expression:", expanded_expr)

# Differentiate the expression with respect to x
diff_expr = sp.diff(expr, x)
print("Differentiated Expression with respect to x:", diff_expr)

# Integrate the expression with respect to x
integral_expr = sp.integrate(expr, x)
print("Integral of the Expression with respect to x:", integral_expr)

# Solve an equation
eq = sp.Eq(x**2 - 4, 0)
solutions = sp.solve(eq, x)
print("Solutions to the equation:", solutions)
