from setuptools import setup

setup(name='resy',
      version='0.1',
      description='python wrapper for Resy API',
      classifiers=[
        'Development Status :: .01 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      url='https://github.com/Satloff/resy_api',
      author='Theo Satloff',
      author_email='theo@satloff.com',
      license='MIT',
      packages=['resy'],
      install_requires=[
          'simplejson',
          'urllib'
      ],
      include_package_data=True,
      zip_safe=False)
