from setuptools import setup


setup(name='ghstars',
      version='1.0',
      description='Show starred repositories',
      author='Maxim',
      author_email='MaximRozhkovv@gmail.com',
      packages=['ghstars'],
      install_requires=['requests', 'argparse'],
      zip_safe=False,
      entry_points={
        'console_scripts':
            ['showstars = ghstars.core:get_from_console']
        }
      )
