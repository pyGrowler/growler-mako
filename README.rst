============
Growler-Mako
============

A Growler RenderEngine for rendering mako_ template files.


Usage
-----

The Growler-Mako package provides the MakoRenderer class exposed at growler.ext.
To use this,

.. code:: python

    # MUST be called like this! You cannot use import growler.ext.MakoRenderer
    from growler.ext import MakoRenderer
    from growler import App

    app = App("MakoTest")

    app.use(MakoRenderer("views/"))
    ...
    @app.get("/")
    def index(req, res):
       res.render("homepage")  # renders views/homepage.mako

.. _mako: http://www.makotemplates.org/
