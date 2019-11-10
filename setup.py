from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='yolov3',
    packages=find_packages(),
    version='0.1.0',
    description='yolov3 implementation from @ultralytics',
    author='ultralytics',
    license='MIT',
    install_requires=required
)
