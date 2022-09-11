from setuptools import setup, find_packages


with open("README.md", "r") as doc:
    long_description = doc.read()

requirements = open("requirements.txt").read().split('\n')


setup(
    # General info
    name = 'sourceforge_demo',
    version = '0.0.1',
    description = 'SF file automation demo',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/exorcistas/py-sourceforge-demo",
    author = "exorcistas",
    author_email = "exorcistas@github.com",

    # Packaging info
    packages=find_packages(),
    install_requires = [requirements],

    # Still don't know how to include requirements to install from remote private repo
    #dependency_links=['git@github.com:exorcistas/sourceforge-scraper.git/master#egg=sourceforge-scraper-0.0.1'],
    
    classifiers = [
        "Programming Language :: Python :: 3.10",
        "Operating System :: Windows"
    ]
)