from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'rki', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='rki_scraper',
      version='0.1.0',
      description='Scrape the RKI Data from Arcgis into a Pandas Dataframe',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['rki'],
      author='Grzegorz Lippe',
      author_email = 'grzegorz.lippe@posteo.de',
      zip_safe=False)
