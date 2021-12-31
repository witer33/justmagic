from distutils.core import setup

setup(
    name='justmagic',
    packages=['justmagic'],
    version='0.0.1',
    license='gpl-3.0',
    description='UFCS in Python',
    author='witer33',
    author_email='dev@witer33.com',
    url='https://github.com/witer33/justmagic/',
    download_url='-',
    keywords=['UFCS'],
    install_requires=[
        'fishhook',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: gpl-3.0 License',
        'Programming Language :: Python :: 3.6',
    ],
)
