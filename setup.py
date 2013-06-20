from distutils.core import setup

setup(
    name='EditREPL',
    version='2013.06.20',
    author='Philip Bjorge',
    author_email='philipbjorge@gmail.com',
    packages=['editrepl'],
    scripts=[],
    url='https://github.com/philipbjorge/EditREPL',
    license='LICENSE.txt',
    description='Use your CLI text editor from within the Python REPL.',
    long_description=open('README_pypi.rst').read()
)
