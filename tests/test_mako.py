#
# tests/test_mako.py
#


import pytest

import growler_mako.mako_renderer
from growler_mako.mako_renderer import MakoRenderer


@pytest.fixture
def renderer():
    return MakoRenderer()


def test_renderer(renderer):
    assert isinstance(renderer, growler_mako.mako_renderer.MakoRenderer)
