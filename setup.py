from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='aws.heywatch',
      version=version,
      description="Access Hey!Watch services from your application",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='heywatch',
      author='Christophe Combelles',
      author_email='christophe.combelles@alterway.fr',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['aws'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.component',
          'restlib',
          'lxml',
          'zope.publisher',
          'zope.contentprovider',
          'zope.app.pagetemplate',
          'zope.interface',
          'zope.component',
          'zope.app.container',
          'zope.traversing',
          'zc.async',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
