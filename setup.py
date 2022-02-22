import pathlib
import sys

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='gpalib',
    version='0.1.3',
    description='A library to convert scores using many arithmetics',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/billchenchina/hitutil',
    author='inclyc',
    author_email='axoford@icloud.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
    keywords='GPA',
    package_dir={'': '.'},
    packages=find_packages(where='.'),
    python_requires='>=3.5, <4',
    install_requires=[],
    project_urls={
        'Bug Reports': 'https://github.com/billchenchina/hitutil/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/billchenchina/hitutil/',
    },
)
