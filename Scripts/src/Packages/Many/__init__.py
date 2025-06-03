# __init__.py
# by lufer

from .Divide import safe_divide, divide
from .Animals import Animal

__all__ = ['safe_divide', 'divide', 'Animal']	#only safe_divide, divide and class Animal are public