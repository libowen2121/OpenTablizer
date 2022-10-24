import setuptools
import importlib

requires = """
addict
"""


def get_requirements():
    ret = [x for x in requires.split("\n") if len(x)>0]
    print("requirements:", ret)
    return ret


setuptools.setup(name='opentablizer',
      version='0.1',
      description="An open source tool for text-to-table",
      long_description="",
      author='Bowen Li, Yuan Yao, Chaojun Xiao',
      author_email='libowen.ne@gmail.com',
      license='Apache',
      packages=setuptools.find_packages(),
      zip_safe=False,
      install_requires=get_requirements(),
      )