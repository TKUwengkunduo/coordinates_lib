from setuptools import setup, find_packages

setup(
    name='coordinate_lib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Kun-Duo,Weng',
    author_email='wengkunduo@gmail.',
    description='A library for coordinate transformations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TKUwengkunduo/coordinate_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
