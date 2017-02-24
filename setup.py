from setuptools import setup, find_packages

setup(
    name="Boids",
    version="1.0",
    description="Birds flocking simulation",
    license="MIT License",
    author="Anestis Mamplekos-Alexiou",
    author_email="anestis.mamplekos-alexiou.16@ucl.ac.uk",
    date="23.2.2017",
    url="https://github.com/anest1s/Refactoring_the_Bad_Boids",
    packages=find_packages(exclude=['*test']),
    scripts=['scripts/boids'],
    install_requires=['argparse', 'numpy', 'matplotlib', 'nose', 'cython', 'pyyaml']
)