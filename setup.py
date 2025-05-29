from setuptools import setup, find_packages

# Leemos los requerimientos desde requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="bora",
    version="0.1.0",
    description="Cliente Python para interactuar con el Boletín Oficial de la República Argentina (BORA).",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Ignacio Ibarra",
    author_email="ignacio_ibarra@hotmail.com",
    url="https://github.com/Ignacio-Ibarra/bora_wrapper",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
)