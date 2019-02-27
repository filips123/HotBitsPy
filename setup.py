from setuptools import setup

def readme():
    with open('README.md') as f:
            return f.read()

setup(
    name = 'hotbits',
    description = 'Python API for HotBits random data generator',
    long_description = readme(),
    long_description_content_type='text/markdown',
    license = 'GPLv3+',

    version_format='{tag}',
    setup_requires=['setuptools-git-version'],

    packages = ['hotbits'],

    entry_points = {
        'console_scripts': ['hotbits=hotbits.__main__:main'],
    },

    extras_require = {
        'lint': ['pylint'],
    },

    python_requires = '>= 3.4',

    author = 'Filip Š',
    author_email = 'projects@filips.si',
    url = 'https://github.com/filips123/HotBitsPy/',
    keywords = 'random-generator, true-random, hotbits, api, generator',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Security :: Cryptography',
    ],

    include_package_data = True,
)
