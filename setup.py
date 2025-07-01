from setuptools import setup, find_packages

setup(
    name='derive-tools',
    version='0.1.0',
    description='Python tools for calculating margin, pricing, and analysis on the (Derive)',
    author='Hoseyn Vafadarali',
    author_email='hoseynvafadarali@gmail.com',
    url='https://github.com/hoseynv/derive-tools',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Office/Business :: Financial',
    ],
    python_requires='>=3.10',
)
