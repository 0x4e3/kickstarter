# coding=utf-8
import os

from setuptools import find_packages, setup

import kickstarter


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Framework :: Django',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10'
]

INSTALL_REQUIREMENTS = [
    'celery>=3.1.0,<4',
    'click>=5.0,<7.0',
    'Django>=1.10.0,<1.10.999',
    'gunicorn>=19.1.0,<19.1.999',
    'psycopg2>=2.7.3,<2.8',
    'raven>=6.1.0,<6.2'
]

setup(
    name='kickstarter',
    version=kickstarter.__version__,
    classifiers=CLASSIFIERS,
    url='',
    license='MIT',
    author='Alexander Lebedev',
    author_email='lebedev@0x4e3.ru',
    description='',
    long_description=open(
        os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    install_requires=INSTALL_REQUIREMENTS,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'kickstarter = kickstarter.runner:main',
        ]
    },
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
)
