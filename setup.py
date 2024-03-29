from setuptools import setup, find_packages

setup(name='blog',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'morepath',
        'waitress',
        'werkzeug',
        'more.chameleon',
      ],
      entry_points= {
        'console_scripts': [
            'morepath-blog = blog.main:prod',
            'moreblog-dev = blog.main:dev',
          ]
      }
)
