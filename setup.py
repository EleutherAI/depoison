import setuptools
setuptools.setup(
    name='depoison',
    version='1.0',
    scripts=['./scripts/depoison'],
    author='Sid Black',
    url='https://github.com/EleutherAI/depoison/',
    description='Fixes poisoned directories in google cloud buckets',
    packages=['lib.depoison'],
    install_requires=['gsutil'],
    python_requires='>=3.5'
)
