from _pre_checks import pre_checks
from logging import getLogger

class pitchfork(pre_checks):
    def __init__(self):
        self._log = getLogger(type(self).__name__)

        super(pitchfork, self).__init__()
