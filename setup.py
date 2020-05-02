# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Sets up params."""
# import datetime
# import os
import sys

from setuptools import find_packages, setup

version = "0.0.1"

project_name = "params-mz"

long_description = """A utility module to load parameters/configs from
dict/json/yaml files provided in the TensorFlow official models. It contains
a parameter dictionary class which supports the nest structure and base
configurations to standardize experiments."""

if "--project_name" in sys.argv:
    project_name_idx = sys.argv.index("--project_name")
    project_name = sys.argv[project_name_idx + 1]
    sys.argv.remove("--project_name")
    sys.argv.pop(project_name_idx)


# def _get_requirements():
#     """Parses requirements.txt file."""
#     install_requires_tmp = []
#     dependency_links_tmp = []
#     with open(
#         os.path.join(os.path.dirname(__file__), "../requirements.txt"), "r"
#     ) as f:
#         for line in f:
#             package_name = line.strip()
#             if package_name.startswith("-e "):
#                 dependency_links_tmp.append(package_name[3:].strip())
#             else:
#                 install_requires_tmp.append(package_name)
#     return install_requires_tmp, dependency_links_tmp


# install_requires, dependency_links = _get_requirements()

# if project_name == "tf-models-nightly":
#     version += ".dev" + datetime.datetime.now().strftime("%Y%m%d")
#     install_requires.append("tf-nightly")
# else:
#     install_requires.append("tensorflow>=2.1.0")

# print("install_requires: ", install_requires)
# print("dependency_links: ", dependency_links)

setup(
    name=project_name,
    version=version,
    description="Params/Configs utility from Tensorflow official models.",
    long_description=long_description,
    author="Google Inc.",
    author_email="no-reply@google.com",
    url="https://github.com/tensorflow/models/hyperparams/",
    license="Apache 2.0",
    packages=find_packages(),
    exclude_package_data={"": ["*_test.py",],},  # noqa
    install_requires=["six", "dataclasses", "typing", "pyyaml"],
    # dependency_links=dependency_links,
    tests_require=["absl", "tensorflow>=2.1.0"],
    python_requires=">=3.7",
)
