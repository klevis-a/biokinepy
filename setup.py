import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='biokinepy',
    version='0.1.2',
    author='Klevis Aliaj',
    author_email='klevis.a@gmail.com',
    description='Utilities for processing, computing, and analyzing joint kinematics.',
    keywords=['biomechanics', 'kinematics', 'kinematic analysis', 'motion capture', 'skin marker', 'quaternion',
              'homogeneous transformation', 'angular velocity'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/klevis-a/biokinepy',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.7',
    install_requires=['numpy', 'numpy-quaternion', 'scipy', 'lazy']
)
