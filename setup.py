from setuptools import find_packages, setup

setup(
    name='monotone',
    packages=find_packages(include="monotone"),
    version="0.1",
    description="Find the minimum of a list which is monotone in nature",
    author="Vineeth V",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    )