# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import spack.config
from spack.cmd.common import arguments
from spack.cmd.compiler import compiler_list

description = "list available compilers"
section = "system"
level = "short"


def setup_parser(subparser):
    subparser.add_argument(
        "--scope",
        choices=arguments.ConfigScopeChoices(),
        metavar=spack.config.SCOPES_METAVAR,
        help="configuration scope to read/modify",
    )


def compilers(parser, args):
    compiler_list(args)
