# Author: Pierre Ablin <pierreablin@gmail.com>
# License: MIT


__version__ = '0.4dev'
from .autoptim import minimize  # noqa
from autograd import numpy


__all__ = [
    "minimize",
    "numpy",
]
