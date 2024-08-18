from setuptools import setup, find_packages

setup(
    name='healthcare-analytics-eda',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'data_processing=src.data_processing:main',
            'visualization=src.visualization:main',
        ],
    },
)
