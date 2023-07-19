from sympy import *
from latex2sympy2 import latex2sympy, latex2latex
from IPython.display import display, Latex
import random


def compareLatexXY(expr, expr_a):
  x, y = symbols('x y')
  expr = sympify(latex2sympy(expr))
  # simplify expr
  expr = expr.simplify()
  # 检查expr是否包含x和y
  if not expr.has(x) or not expr.has(y):
    print("本函数仅用于比较含有x和y的表达式")
    return False
  # 检查expr中是否包含除了x和y以外的其他变量
  if len(expr.free_symbols) > 2:
    print("本函数仅用于比较含有x和y的表达式")
    return False

  expr_a = sympify(latex2sympy(expr_a), evaluate=False)

  # Expand the expressions and get the coefficients
  coeffs1 = expr.expand().as_coefficients_dict()
  coeffs2 = expr_a.expand().as_coefficients_dict()
  same = True
  if coeffs1 != coeffs2:
    print("等式不相同")
    same = False

  if len(str(expr_a).replace(" 1*", "")) > len(str(expr)):
    print("未简化")
    same = False

  return same
