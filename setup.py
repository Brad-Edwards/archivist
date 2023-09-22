from setuptools import setup, find_packages
from src.archivist import __app_name__, __version__

setup(
    name=__app_name__,
    description="Archivist is a tool for understanding codebases.",
    long_description=open('README.md').read(),
    author='Brad Edwards',
    author_email='j.bradley.edwards@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Software Architecture :: Code Review',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    version=__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'archivist = src.archivist.__main__:main',
        ],
    },
)
