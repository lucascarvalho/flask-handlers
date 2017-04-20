# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def local_file(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read()


if __name__ == '__main__':
    setup(
        name="flask-handlers",
        version='0.0.1',
        description="Handlers for Flask applications",
        long_description=local_file('README.md'),
        author='Lucas Carvalho',
        author_email='lucascarvalho@gmail.com',
        url='https://github.com/lucascarvalho/flask-handlers',
        packages=find_packages(exclude=['*tests*']),
        install_requires=[],
        include_package_data=True,
        dependency_links=[],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        zip_safe=False,
    )
