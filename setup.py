from setuptools import setup, find_packages

setup(
    name='healthcare-analytics-eda',
    version='0.1',
    packages=find_packages(),  # Automatically finds all packages and sub-packages
    install_requires=[
        'pandas',      # Data manipulation library
        'matplotlib',  # Plotting library
        'seaborn',     # Statistical data visualization library
        'jupyter',     # Jupyter notebook support
    ],
    description='Exploratory Data Analysis of Healthcare Data',
    author='Seid-M-Adem',                    # Replace with your name
    author_email='seid.adem@gmx.ch',  # Replace with your email address
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
