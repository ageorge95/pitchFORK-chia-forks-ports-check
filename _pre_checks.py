from json import load,\
    dump
from logging import getLogger
from os import path,\
    getcwd
from sys import exit

from _base import std_names,\
    cfg_paths_template

class pre_checks():

    _log: getLogger
    override_paths_list: list

    def __init__(self):
        super(pre_checks, self).__init__()

        self.input_raw = None

        final_verdict_helper = []
        for test in [self.check_input_json_integrity,
                     self.check_valid_filepaths]:
            final_verdict_helper += test()

        final_verdict = list(filter(lambda x: x['test'] == std_names.FAILED_TEST, final_verdict_helper))
        if len(final_verdict) > 0:
            self._log.error('Pre-checks failed. Cannot continue !')
            for message in final_verdict:
                self._log.info(message['reason'])
            exit()
        self._log.info('Pre checks PASSED')

    def check_input_json_integrity(self):
        to_return = []
        if not self.override_paths_list:
            if not path.isfile(path.join(getcwd(), 'input.json')):
                user_home = path.expanduser("~")
                with open(path.join(getcwd(), 'input.json'), 'w') as json_out_handle:
                    dump({"cfg_paths": [entry.format(user_home=user_home) for entry in cfg_paths_template]}, json_out_handle, indent=2)
                self._log.info('input.json missing. Was created in {}'.format(path.join(getcwd(), 'input.json')))
            try:
                with open(path.join(getcwd(), 'input.json'), 'r') as json_in_handle:
                    self.input_raw = load(json_in_handle)
            except:
                to_return.append({'test': std_names.FAILED_TEST,
                                  'reason': 'input.json integrity check failed !'})
        else:
            self.input_raw = 'bypassed'
        return to_return if len(to_return) > 0 else [{'test': std_names.PASSED_TEST,
                                                      'reason': None}]

    def check_valid_filepaths(self):
        to_return = []
        self.input_paths_checked = []

        if self.input_raw:
            for cfg_filepath in (self.input_raw['cfg_paths'] if not self.override_paths_list else self.override_paths_list):
                if cfg_filepath not in self.input_paths_checked:
                    if path.isfile(cfg_filepath):
                        self.input_paths_checked.append(cfg_filepath)
                    else:
                        self._log.warning('Ignored invalid path: {}'.format(cfg_filepath))
                else:
                    self._log.warning('Ignored duplicate path: {}'.format(cfg_filepath))

        if len(self.input_paths_checked) == 0:
            to_return.append({'test': std_names.FAILED_TEST,
                              'reason': 'all input paths are not accessible'})
        return to_return if len(to_return) > 0 else [{'test': std_names.PASSED_TEST,
                                                      'reason': None}]
