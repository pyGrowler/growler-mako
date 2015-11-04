#
# growler_ext/MakoRenderer.py
#
"""
Loader script for the MakoRenderer class.

This script overloads the expected module object with the class MakoRenderer.
"""

import sys
from growler_mako.mako_renderer import MakoRenderer

sys.modules[__name__] = MakoRenderer
