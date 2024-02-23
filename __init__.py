from .nums_pattern import append_nums, append_nums_all, prepend_nums, prepend_nums_all
from .pattern import apply_patterns, apply_patterns_all
from .substitution import substitute, substitute_all
from .variations import generate_variations

from .utils import generate_base_wordlist

__all__ = [
    'append_nums', 'append_nums_all', 'prepend_nums', 'prepend_nums_all',
    'apply_patterns', 'apply_patterns_all',
    'substitute', 'substitute_all',
    'generate_variations',
    'generate_base_wordlist'
]

__version__ = "1.1"

