from setuptools import setup

setup(name="paddocks", version="1.0.0", packages=["paddocks"],
      entry_points={'console_scripts': ["paddocks = paddocks.__main__:main"]
                    })
