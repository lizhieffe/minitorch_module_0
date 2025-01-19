"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Any, Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:

EPS = 1e-6

# - mul
def mul(a: float, b: float) -> float:
  return a * b

# - id
def id(a) -> float:
  return a

# - add
def add(a: float, b: float) -> float:
  return a + b

# - neg
def neg(a: float) -> float:
  return -1 * a

# - lt
def lt(a: float, b: float) -> float:
  return a < b

# - eq
def eq(a, b):
  return a == b

# - max
def max(a, b):
  if a > b:
    return a
  else:
    return b

# - is_close
# - sigmoid
# - relu
# - log
# - exp

# - log_back
def log_back(a, b):
  return b / (a + EPS)

# - inv
def inv(a: float) -> float:
  return 1.0 / a

# - inv_back
def inv_back(a, b):
  return -(1.0 / a ** 2) * b

# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement

# - negList : negate a list
def negList(a: list[Any]) -> list[Any]:
  return [-1 * it for it in a]

# - addLists : add two lists together
def addLists(a: list[float], b: list[float]) -> list[float]:
  return [ea + eb for ea, eb in zip(a, b)]

# - sum: sum lists

# - prod: take the product of lists
def prod(a: list[Any], b: list[Any]) -> list[Any]:
  return [ae * be for ae, be in zip(a, b)]


# TODO: Implement for Task 0.3.
