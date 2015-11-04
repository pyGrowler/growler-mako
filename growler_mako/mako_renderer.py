#
# growler_mako/mako_renderer.py
#

import logging
from mako.template import Template


class MakoRenderer:
    """
    Renderer middleware for mako templates
    """

    DEFAULT_FILE_EXTENSIONS = [
        '.mako',
    ]

    def __init__(self):
        self._render = Template

        self.log = logging.getLogger(__name__)
        self.log.info("{} Constructed MakoRenderer".format(id(self)))

    def __call__(self, filename, res):
        self.log.info("%d -> %s" % (id(self), filename))
        tmpl = self._render(filename=filename)
        html = tmpl.render()
        return html

    @staticmethod
    def register_engine():
        """
        Add this rendering engine to the standard growler renderer
        """

        import growler.middleware.renderer
        growler.middleware.renderer.render_engine_map['mako'] = MakoRenderer
