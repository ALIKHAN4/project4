from setuptools import setup, find_packages


def get_requirements(file_path):
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        [r.replace('/n','') for r in requirements]
    return requirements


setup(
    name = 'project4',
    version='0.0.1',
    description='this is test project for ml applications',
    author_email='alikhan680880@gmail.com',
    packages=find_packages(),
    install_require = get_requirements('requirements.txt')
)