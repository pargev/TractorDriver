import markdown as markdown
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
requirements_file_location = os.path.join(here, 'requirements.txt')


def parse_read_me():
    readme_file_location = os.path.join(here, 'README.md')
    with open(readme_file_location, 'r') as readme:
        file_string = readme.read()
        return markdown.markdown(file_string)


README = parse_read_me()


def parse_requirements(reqs):
    with open(reqs) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]


requirements = parse_requirements(requirements_file_location)

setup(
    name='tractordriver',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='Pargev Ghazaryan\'s License',
    author='Pargev Ghazaryan',
    author_email='pargev.ghazarian@gmail.com',
    description='Angular test automation with python',
    install_requires=requirements,
    long_description=README,
    include_package_data=True,
    package_data={'': ['clientsidescripts.js']},

)
