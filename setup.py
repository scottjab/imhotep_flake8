from setuptools import setup, find_packages

setup(
    name='imhotep_flake8',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/scottjab/imhotep_flake8',
    license='MIT',
    author='James Scott',
    author_email='scottjab@gmail.com',
    description='An imhotep plugin for python validation',
    install_requires=["flake8"],
    entry_points={
        'imhotep_linters': [
            '.py = imhotep_flake8.plugin:Flake8Linter'
        ],
    },
)
