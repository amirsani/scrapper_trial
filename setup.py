from setuptools import setup
import os

VERSION = "0.13"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="scrapper_trial",
    description="Tools for taking automated screenshots of websites",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/aramns1089/scrapper_trial",
    project_urls={
        "Issues": "https://github.com/aramns1089/scrapper_trial/issues",
        "CI": "https://github.com/aramns1089/scrapper_trial/actions",
        "Changelog": "https://github.com/aramns1089/scrapper_trial/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["scrapper_trial"],
    entry_points="""
        [console_scripts]
        shot-scraper=shot_scraper.cli:cli
    """,
    install_requires=["click", "PyYAML", "playwright", "click-default-group"],
    extras_require={"test": ["pytest", "cogapp", "pytest-mock"]},
    python_requires=">=3.7",
)
