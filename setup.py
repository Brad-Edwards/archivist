from setuptools import setup, find_packages
setup(
    name='archivist',
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
    version='0.1.0',
    packages=find_packages(),
)
