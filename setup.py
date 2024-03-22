from setuptools import setup, find_packages

setup(
  name = 'pytorch-ml-utils',
  packages = find_packages(exclude=[]),
  version = '0.1.0',
  license='MIT',
  description = 'Pytorch ML Utils',
  author = 'Tuan-Vu Trinh',
  author_email = 'tuanvutrinh.ai@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/trinhtuanvubk/pytorch-ml-utils',
  keywords = [
    'pytorch',
    'accelerate',
    'utils'
  ],
  install_requires=[
    'accelerate',
    'optree',
    'pytorch-warmup',
    'torch>=2.0'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
  ],
)