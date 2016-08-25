from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='images2gif',
    version='1.0.0',
    description='Python 3 compatible images2gif.py',
    long_description=long_description,
    url='https://github.com/isaacgerg/images2gif',
    author='Almar Klein, Ant1, Marius van Voorden',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
    ],
    py_modules=['images2gif'],
    install_requires=['numpy>=1.11.1', 'Pillow>=3.3.1', 'scipy>=0.18.0'],
)
