"""
Configuration du paquet Frython.
"""

from setuptools import setup, find_packages
import os

def lire_readme():
    chemin = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(chemin, 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='frython',
    version='1.0.2',
    author='Arthur Godart',
    author_email='official.frython@gmail.com',
    description='🐓 Python en français, sacré bleu !',
    long_description=lire_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Artleboss2/frython',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Interpreters',
        'Natural Language :: French',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'frython=frython.__main__:main',
        ],
    },
    keywords='python français french programming language transpiler',
    project_urls={
        'Bug Reports': 'https://github.com/Artleboss2/frython/issues',
        'Source': 'https://github.com/Artleboss2/frython',
        'Documentation': 'https://github.com/Artleboss2/frython#readme',
    },
)
