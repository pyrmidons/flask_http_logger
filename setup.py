from setuptools import setup, find_packages

exclude = [
    'tests',
    'tests.*',
        ]

exec(open('./flask-http-logger/version.py').read())

with open('README.md', encoding='utf-8') as readmef:
    long_description = readmef.read()

setup(
    name='Flask-HTTP-Logger',
    version=__version__,
    url='',
    license='MIT',
    author='Giorgi, Goga',
    author_email='ent1c3d@gmail.com',
    description='Flask Http Logger',
    long_description=long_description,
    keywords = ["http", "logger", "flask"],
    packages=find_packages(exclude=exclude),
    include_package_data=True,
    platforms='any',
    zip_safe=False,
    setup_requires=[
        'pytest-runner==4.2',
    ],
    tests_require=[
        'coverage==4.5.1',
        'pydocstyle>=1.0.0',
        'pytest-cache>=1.0',
        'pytest-cov>=2.6.0',
        'pytest-pep8>=1.0.6',
        'pytest>=3.7.4',
    ],
    install_requires=[
        'Flask==1.0.2'
    ],
    classifiers=[
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ]
)
