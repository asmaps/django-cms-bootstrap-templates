# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-cms-bootstrap-templates',
    version='0.0.2a',
    author=u'Arne Schauf',
    author_email='python.asmaps.de',
    packages=['cms_bootstrap_templates'],
    url='https://github.com/asmaps/django-cms-bootstrap-templates',
    license='MIT licence, see LICENCE file',
    description='A set of bootstrap3 templates for use with django-cms',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True
)
