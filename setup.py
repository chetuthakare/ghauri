import os
from setuptools import setup, find_packages

setup(
    name="ghauri",
    version="1.5.0",
    description="An advanced SQL injection detection & exploitation tool with AI-powered accuracy enhancements.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
    ],
    author="Nasir Khan",
    author_email="r0oth3x49@gmail.com",
    packages=find_packages(),
    package_data={"": ["data/*.json", "models/*.pkl"]},
    include_package_data=True,
    zip_safe=False,
    test_suite="ghauri",
    install_requires=[
        "tldextract",
        "colorama",
        "requests",
        "chardet",
        "ua_generator",
        "numpy",  # For numerical computations
        "pandas",  # For data manipulation
        "scikit-learn",  # For AI/ML model integration
        "joblib",  # For saving/loading trained models
    ],
    extras_require={
        "dev": ["pytest", "black"],  # Developer tools
    },
    entry_points={"console_scripts": ["ghauri=ghauri.scripts.ghauri:main"]},
    keywords=[
        "mysql",
        "mssql",
        "oracle",
        "postgre",
        "sql",
        "injection",
        "boolean-based",
        "time-based",
        "error-based",
        "stacked-queries",
        "ai",
        "machine-learning",
        "cybersecurity",
    ],
    python_requires=">=3.6",
)
