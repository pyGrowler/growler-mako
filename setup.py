#
# setup.py
#
"""
An extension providing a mako renderer for growler applications
"""

from os import path
from glob import glob
from setuptools import setup, find_packages
from imp import load_source

NAME = 'growler-mako'

REQUIRES = [
    'mako',
]

OPTIONAL_REQUIRES = {
}

TESTS_REQUIRE = [
    'pytest',
    'pytest-asyncio',
]

PACKAGES = [
    'growler_mako',
    'growler_ext.mako_renderer',
    'growler_ext.MakoRenderer',
]

NAMESPACES = [
    'growler_ext',
]

CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Environment :: Web Environment",
    "Operating System :: OS Independent",
    # "Framework :: Growler",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Internet :: WWW/HTTP",
    "Natural Language :: English",
]

metafile = path.join(".", "growler_mako", "__meta__.py")
metadata = load_source("metadata", metafile)

tar_url = 'https://github.com/pygrowler/growler-mako/archive/v%s.tar.gz' % (metadata.version)  # noqa

setup(
    name=NAME,
    version=metadata.version,
    author=metadata.author,
    license=metadata.license,
    url=metadata.url,
    download_url=tar_url,
    author_email=metadata.author_email,
    description=__doc__.strip(),
    classifiers=CLASSIFIERS,
    install_requires=REQUIRES,
    extras_require=OPTIONAL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    packages=PACKAGES,
    namespace_packages=NAMESPACES,
    platforms='all',
    scripts=glob('scripts/*')
)
