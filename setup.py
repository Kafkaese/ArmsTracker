from setuptools import setup



with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='ArmsTracker',
      version="1.0",
      description="Project Description",
      packages=['taro'],
      install_requires=requirements
      )
