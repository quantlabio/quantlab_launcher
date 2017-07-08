# coding: utf-8
"""Jupyter QuantLab Launcher"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
from notebook.notebookapp import NotebookApp
from traitlets import Unicode

from .handlers import add_handlers, LabConfig


class LabLauncherApp(NotebookApp):

    default_url = Unicode('/quatlab',
        help="The default URL to redirect to from `/`")

    lab_config = LabConfig()

    def start(self):
        add_handlers(self.web_app, self.lab_config)
        super.start()


main = LabLauncherApp.launch_instance
