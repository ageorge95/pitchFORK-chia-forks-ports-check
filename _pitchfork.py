from _pre_checks import pre_checks
from logging import getLogger
from concurrent.futures import ThreadPoolExecutor
from yaml import safe_load
from traceback import format_exc

class pitchfork(pre_checks):
    def __init__(self):
        self._log = getLogger(type(self).__name__)

        super(pitchfork, self).__init__()

    def parse_cfg_slave(self,
                        valid_path):

        try:
            with open(valid_path, 'r') as yaml_in_handle:
                to_return = safe_load(yaml_in_handle)
                self._log.info('Successfully parsed {}'.format(valid_path))
                return to_return
        except:
            self._log.warning('Failed to parse {}'.format(valid_path))
            self._log.debug(format_exc(chain=False))

    def parse_all_cfgs(self,
                       override_paths: list = None):
        if not override_paths: override_paths = self.input_paths_checked

        self.contents = []
        with ThreadPoolExecutor(10) as exec_pool:
            for valid_path in override_paths:
                self.contents.append(exec_pool.submit(self.parse_cfg_slave,(valid_path)))
