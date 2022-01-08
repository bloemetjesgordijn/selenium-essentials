import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="selenium-essentials",
    version="1.0.2",
    description="Speed up selenium development",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bloemetjesgordijn/selenium-essentials",
    author="Bloemetjesgordijn",
    author_email="casbertrams@live.nl",
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    packages=["selenium-essentials"],
    include_package_data=True,
    install_requires=["selenium", "random", "time"]
)