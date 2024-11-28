"""Setuptools script."""
import os
from setuptools import setup, find_packages


setup(
    name="ghauri",
    version="1.5.0",  # New version for AI feature
    description="An advanced SQL injection detection & exploitation tool with AI-powered accuracy.",
    classifiers=["Programming Language :: Python3"],
    author="Nasir Khan",
    author_email="r0oth3x49@gmail.com",
    packages=find_packages(),
    package_data={"": []},
    include_package_data=True,
    zip_safe=False,
    test_suite="ghauri",
    install_requires=[
        "tldextract",          # Domain extraction
        "colorama",            # Colorful terminal output
        "requests",            # HTTP requests
        "chardet",             # Character encoding detection
        "ua_generator",        # User agent generation
        "scikit-learn",        # Machine learning library (for training models)
        "tensorflow",          # Deep learning framework (for advanced models)
        "nltk",                # Natural Language Toolkit (for NLP)
        "pandas",              # Data manipulation (for model training)
        "numpy",               # Numerical operations
    ],
    entry_points={"console_scripts": ["ghauri=ghauri.scripts.ghauri:main"]},
    keywords=[
        "mysql", "mssql", "oracle", "postgre", "sql", "injection", "boolean-based",
        "time-based", "error-based", "stacked-queries", "AI", "machine learning"
    ],
    python_requires=">=3.6",
)
