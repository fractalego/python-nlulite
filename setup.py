from setuptools import setup

setup(name='pynsett',
      version='0.0.8',
      description='A relation extractor',
      url='http://github.com/fractalego/pynsett',
      author='Alberto Cetoli',
      author_email='alberto@nlulite.com',
      license='MIT',
      packages=['pynsett',
                'pynsett.auxiliary',
                'pynsett.discourse',
                'pynsett.drt',
                'pynsett.examples',
                'pynsett.extractor',
                'pynsett.inference',
                'pynsett.install',
                'pynsett.knowledge',
                'pynsett.metric',
                'pynsett.nl',
                'pynsett.tests',
                'pynsett.writer',
                ],
      install_requires=[
          'spacy==1.8.0',
          'python-igraph',
          'nltk==3.2.1',
          'rdflib',
          'yappi',
          'gensim',
          'more_itertools',
          'parvusdb==0.0.18',
          'hy',
      ],
      include_package_data=True,
      zip_safe=False)
