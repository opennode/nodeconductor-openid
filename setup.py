#!/usr/bin/env python
import sys
from setuptools import setup, find_packages


dev_requires = [
    'Sphinx==1.2.2',
]

install_requires = [
    'django-openid-auth',
    'nodeconductor>=0.96.0',
]


setup(
    name='nodeconductor-openid',
    version='0.1.0.dev0',
    author='OpenNode Team',
    author_email='info@opennodecloud.com',
    url='http://nodeconductor.com',
    description='NodeConductor plugin bringing OpenID-based authentication support.',
    long_description=open('README.rst').read(),
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=install_requires,
    zip_safe=False,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'nodeconductor_extensions': (
            'nodeconductor_openid = nodeconductor_openid.extension:NodeConductorOpenIDExtension',
        ),
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
)