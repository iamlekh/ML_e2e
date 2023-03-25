from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    Reads a file containing package requirements and returns a list of strings,
    where each string represents a package name.

    Args:
        file_path: A string representing the path to the file containing the package requirements.

    Returns:
        A list of strings representing the package names.

    Raises:
        FileNotFoundError: If the file at file_path does not exist.
    """
    requirements = []
    # Read the file and remove newlines
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if present (used in some development packages)
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Darpan",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
