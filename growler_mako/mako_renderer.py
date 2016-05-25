#
# growler_mako/mako_renderer.py
#

import pathlib
from mako.template import Template as MakoTemplate
from growler.middleware.renderer import RenderEngine


class MakoRenderer(RenderEngine):
    """
    Renderer middleware for mako templates
    """

    default_file_extensions = [
        '.mako',
        '.html.mako',
    ]

    def __init__(self, *args, **kwargs):
        """
        Create renderer. Currently all arguments are forwarded to the
        superclass.
        """
        super().__init__(*args, **kwargs)
        self.template_cache = {}

    def load_and_cache_template(self, path, mtime):
        """
        Reads the file at pathlib.Path path and stores the generated
        content, along with modified time, in the template cache,
        and returning the template.
        """
        try:
            template = MakoTemplate(path.read_text())
        except AttributeError:
            with open(str(path), 'r') as file:
                template = MakoTemplate(file.read())
        self.template_cache[path] = mtime, template
        return template

    def render_source(self, filename, obj={}):
        """
        Renders the template found at 'filename'.

        Args:
            filename (str or pathlib.Path): Path to the template file
            obj (dict): Dictionary of data to pass to the templating engine
        """
        filename = pathlib.Path(filename).resolve()
        stat = filename.stat()
        try:
            cache_mtime, template = self.template_cache[filename]
            if stat.st_mtime > cache_mtime:
                template = self.load_and_cache_template(filename, stat.st_mtime)
        except KeyError:
            template = self.load_and_cache_template(filename, stat.st_mtime)

        return template.render(**obj)
