import os
import setuptools

setuptools.setup(
    name='theanets',
    version='0.1.0',
    packages=setuptools.find_packages(),
    author='Leif Johnson',
    author_email='leif@leifjohnson.net',
    description='A library of neural nets in theano',
    long_description=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')).read(),
    license='MIT',
    url='http://github.com/lmjohns3/theano-nets/',
    keywords=('deep-belief-network '
              'neural-network '
              'theano '
              'machine-learning'),
    install_requires=['theano', 'lmj.cli'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        ],
    )
