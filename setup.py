from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='Twitter=Bot',
      version='1.0.5',
      description='Just another twitter bot',
      url='https://github.com/jammie080/Twitter-Bott',
      author='Jammie Messam',
      author_email='diycertified@aol.com',
      license='MIT',
      packages=['Twitter-Bot'],
      long_description=read('README'),
      zip_safe=False)