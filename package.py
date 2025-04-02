name = "libpng"

version = "1.6.43.hh.1.0.0"

authors = [
    "Cosmin Truta",
]

description = """PNG reference library"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = []

private_build_requires = []

variants = []


def commands():
    env.REZ_LIBPNG_ROOT = "{root}"
    env.LIBPNG_ROOT = "{root}"
    env.PNG_ROOT = "{root}"
    env.PNG_LOCATION = "{root}"
    env.PATH.append("{root}/bin")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")


uuid = "repository.libpng"
