from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='hr',
    version="0.1.0",
    description="CLI user management utility",
    author="Felipe Gusmao",
    author_email="fgmonad@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)