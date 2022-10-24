from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="gillespie",
    version="0.0.2",
    description="Pure Python implementation of the Gillespie algorithm for stochastic simulations.",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_dir={"gillespie": "src"},
    packages=["gillespie"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    url="https://github.com/sueskind/gillespie",
    author="sueskind",
    author_email="52210599+sueskind@users.noreply.github.com"
)
