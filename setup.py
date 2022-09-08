from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-PIDBoilPWM',
      version='0.0.1',
      description='CraftBeerPi4 PID Kettle Control Plugin with PWM output',
      author='Jens Brand',
      author_email='jens.brand@ersrode.de',
      url='https://github.com/jens-brand/cbpi4-PIDBoilPWM',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-PIDBoilPWM': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-PIDBoilPWM'],
	  long_description=long_description,
	  long_description_content_type='text/markdown'
     )
