from setuptools import setup, find_packages

setup(
    name='botX',
    version='1.0.0',
    description='A ROS wrapper',
    url='https://github.com/tianhaoz95/botX',
    author='Jason Chiau',
    author_email='tyan_chiau@berkeley.edu',
    scripts=['bin/botX'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Robotics',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests', 'examples'])
)
