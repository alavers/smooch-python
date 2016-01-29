from setuptools import setup
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'LONG_DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='smooch',
    version='0.0.1',
    description='Smooch Python SDK',
    long_description=long_description,
    url='https://github.com/alavers/smooch-python',
    author='Andrew Lavers',
    author_email='andrew@smooch.io',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Operating System :: OS Independent"
    ],
    keywords='smooch messaging',
    packages=['smooch', 'smooch.test'],
    install_requires=['requests >= 0.8.8'],
    test_suite='smooch.test.all',
    tests_require=['unittest2', 'mock == 1.0.1']
)
