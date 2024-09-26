# Copyright (C) 2024, twiinIT
# SPDX-License-Identifier: BSD-3-Clause

import os
from pathlib import Path
from subprocess import run
from urllib.request import urlopen

from setuptools import setup
from setuptools.command.build_py import build_py

from antlr4_cli import __version__


class DownloadANTLR(build_py):
    """Generates the ANTLR4 runtime from grammar file."""

    def run(self):

        with urlopen(
            f"https://repo1.maven.org/maven2/org/antlr/antlr4/{__version__}/antlr4-{__version__}-complete.jar",
            timeout=60,
        ) as response:
            print(f"Downloading antlr4-{__version__}-complete.jar")
            s = response.read()

            with open(Path("antlr4_cli") / f"antlr4-{__version__}", "wb") as f:
                f.write(s)

        super().run()


setup(
    cmdclass={
        "build_py": DownloadANTLR,
    },
    entry_points={
        "console_scripts": [
            "antlr4=antlr4_cli:tool",
            "antlr4-parse=antlr4_cli:interp",
        ]
    },
)
