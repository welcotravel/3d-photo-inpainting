from setuptools import setup
from setuptools import find_packages

setup(
  name='photo_3d',
  version='0.1.0',
  description='3d photo inpainting',
  url='https://github.com/welcome/3d-photo-inpainting',
  author='victusfate',
  author_email='messel@gmail.com',
  license='MIT',
  packages=find_packages(),
  install_requires = [
    'imageio==2.9.*',
    'torch==1.4.0',
    'torchvision==0.5.0',
    'opencv-python==4.2.0.32',
    'vispy==0.6.4',
    'moviepy==1.0.2',
    'transforms3d==0.3.1',
    'networkx==2.3',
    'matplotlib',
    'absl-py==0.9.0',
    'asyncio',
    'aiohttp',
    'aiofiles',
    'networkx==2.3',
    'scikit-image',
    'Cython==3.0a3',
    'decorator==4.4.2',
    'cynetworkx'
  ],
  package_data={'photo_3d': ['argument.yml','download.sh']},
  zip_safe=False
)
