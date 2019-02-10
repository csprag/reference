from setuptools import setup

setup(
    name='CSP Reference Page',
    packages=['reference'],
    include_package_data=True,
    install_requires=[
        'flask',
        'cython',
        'mistune',
        'Pygments',
        'gunicorn',
    ],
)
