from setuptools import setup, find_packages

setup(
    name="df_squeezer",
    version="0.0.6",
    author="Perttu Isotalo, Kenneth Breugelmans",
    author_email="perttu.isotalo@gmail.com, kennethbreugelmans@gmail.com",
    description="A small package to optimize memory usage of Pandas DataFrames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dscients/squeezer",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
