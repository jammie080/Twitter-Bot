from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='Twitter=Bot',
      version='1.0.5.3',

      description='Just another twitter bot',

      url='https://github.com/jammie080/Twitter-Bot',

      author='Jammie Messam',

      author_email='diycertified@aol.com',

      license=read('LICENSE'),

      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7'

    ],

      keywords='twitter bot development',

      packages=find_packages(exclude=('examples', 'settings','twitter')),

      install_requires=[
      'BeautifulSoup>=3.2.1',
      'selenium>=2.53.6',
      'python-dotenv>=0.6.0'],

      long_description=read('README.md'),

      zip_safe=False)