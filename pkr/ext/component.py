# -*- coding: utf-8 -*-
# Copyright© 1986-2018 Altair Engineering Inc.

"""Component extensions allows to use a generic env and pass its name when creating a Kard"""

from __future__ import absolute_import

from builtins import str
import os

from git import Repo

from pkr.cli.log import write
from . import ExtMixin


class Component(ExtMixin):
    """Mixin for an extension implementation"""

    @staticmethod
    def setup(args, kard):
        """Populate kard with component name

        Args:
          - args: the args passed in the env
          - kard: the kard object
        """
        component_name = args.get('component_name', kard.meta.get('component_name'))
        if component_name is not None:
            k8sfiles = kard.env['driver']['k8s']['k8s_files']
            k8sfiles = [t.format(component_name=component_name) for t in k8sfiles]
            kard.env['driver']['k8s']['k8s_files'] = k8sfiles

    @staticmethod
    def populate_kard():
        """Populate kard folder"""

