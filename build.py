#! /usr/bin/python3.5

from distutils.core import setup, Extension


setup(ext_modules=[Extension("ctrie", ["trie.c"],
                             extra_compile_args=["-g", "-O0"])])
