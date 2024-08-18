from setuptools import setup, find_packages

setup(
    name='healthcare-analytics-eda',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'jupyter',
    ],
    description='Exploratory Data Analysis of Healthcare Data',
    author='Seid M Adem',
    author_email='seid.adem@gmx.ch',
)

