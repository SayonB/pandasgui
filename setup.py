from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='pandasgui',
      version='0.1.12',
      description='A GUI for Pandas DataFrames.',
      author='Adam Rose',
      author_email='adam.e.rose@hotmail.com',
      url='https://github.com/adamerose/pandasgui',
      packages=find_packages(),
      include_package_data=True,
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=[
          'pandas',
          'PyQt5',
          'PyQtWebEngine',
          'seaborn',
          'plotly']
      )
