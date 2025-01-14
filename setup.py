import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutork8s_deploy_tasks", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-k8s-deploy-tasks",
    version=ABOUT["__version__"],
    url="https://github.com/myusername/tutor-contrib-k8s-deploy-tasks",
    project_urls={
        "Code": "https://github.com/myusername/tutor-contrib-k8s-deploy-tasks",
        "Issue tracker": "https://github.com/myusername/tutor-contrib-k8s-deploy-tasks/issues",
    },
    license="AGPLv3",
    author="Lawrence McDaniel",
    description="k8s_deploy_tasks plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["tutor"],
    entry_points={
        "tutor.plugin.v1": [
            "k8s_deploy_tasks = tutork8s_deploy_tasks.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
