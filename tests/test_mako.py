#
# tests/test_mako.py
#

import time
import pytest
import growler
import pathlib
import growler_mako.mako_renderer

from unittest import mock
from growler_mako.mako_renderer import MakoRenderer

@pytest.fixture
def template_path(tmpdir):
    foo = tmpdir.join("foo.mako")
    foo.write("hello foo")
    return pathlib.Path(str(foo))


@pytest.fixture
def renderer(tmpdir):
    return MakoRenderer(str(tmpdir))


def test_renderer(renderer):
    assert isinstance(renderer, growler_mako.mako_renderer.MakoRenderer)


def test_renderer_renders(renderer, template_path):
    tmpl = template_path
    assert renderer.render_source(tmpl) == 'hello foo'


def test_render_works_with_growler(renderer):
    req, res = mock.Mock(), mock.Mock()
    del res.render
    renderer(req, res)
    assert isinstance(res.render, growler.middleware.renderer.Renderer)
    assert not req.called


def test_render_renders_with_path(renderer, template_path):
    req, res = mock.Mock(), mock.Mock()
    del res.render
    renderer(req, res)
    res.render("foo.mako")

    res.send_html.assert_called_with("hello foo")
    assert str(template_path) == str(list(renderer.template_cache.keys())[0])


def test_render_renders_with_path_and_object(renderer, tmpdir, template_path):
    tmpdir.join("foo.mako").write("hello, ${name}!")

    req, res = mock.Mock(), mock.Mock()
    del res.render
    renderer(req, res)

    res.render("foo", {'name': 'Jack'})

    res.send_html.assert_called_with("hello, Jack!")


def test_render_caches(renderer, tmpdir, template_path):
    tmpdir.join("foo.mako").write("hello, ${name}!")

    req, res = mock.Mock(), mock.Mock()
    del res.render
    renderer(req, res)
    res.render("foo.mako", {'name': 'Jack'})
    # time.sleep(0.1)
    template_path.touch()
    res.render("foo.mako", {'name': 'Jack'})

    res.send_html.assert_called_with("hello, Jack!")
