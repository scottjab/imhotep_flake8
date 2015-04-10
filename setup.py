from setuptools import setup, find_packages

setup(
    name='imhotep_flake8',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/scottjab/imhotep_flake8',
    license='MIT',
    author='James Scott',
    author_email='scottjab@gmail.com',
    description='An imhotep plugin for python validation',
    entry_points={
        'imhotep_linters': [
            '.py = imhotep_flake8.plugin:Flake8Linter'
        ],
    },
)
