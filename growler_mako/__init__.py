#
# growler_mako/__init__.py
#
"""
Package for mako rendering engine for Growler framework
"""

from .__meta__ import (
    version as __version__,
    date as __date__,
    author as __author__,
    license as __license__,
)

from .mako_renderer import MakoRenderer
