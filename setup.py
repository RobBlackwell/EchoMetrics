from distutils.core import setup

setup(
    name='EchoMetrics',
    version='0.1.0',
    author='Sam Urmy',
    author_email='sam.urmy@gmail.com',
    packages=['echometrics', 'echometrics.tests'],
    package_data={'echometrics' : ['data/*']},
    license='LICENSE.txt',
    description='Acoustic water column metrics',
    long_description=open('README.md').read(),

)
