from setuptools import setup


setup(
    name='oh-shgit',
    version='0.1',
    py_modules=['oh-shgit'],
    author="Mehmet Çağatay Barın",
    author_email="mcagataybarin@gmail.com",
    url="https://github.com/mcbarin/oh-shgit",
    description=("""Helper package for beginners who just started to use GitHub"""),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        oh-shgit=oh-shgit:main
    '''
)
