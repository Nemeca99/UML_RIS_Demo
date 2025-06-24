"""
Setup script for UML Calculator Community Edition
"""
from setuptools import setup, find_packages

setup(
    name="uml-calculator",
    version="0.1.0",
    description="UML Calculator combines standard mathematics with UML diagram generation",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "rich>=10.0.0",
        "typer>=0.4.0",
        "sympy>=1.8",
        "numpy>=1.20.0",
        "matplotlib>=3.4.0",
        "pydot>=1.4.2",
        "graphviz>=0.16"
    ],
    entry_points={
        "console_scripts": [
            "umlcalc=calculator:app",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
