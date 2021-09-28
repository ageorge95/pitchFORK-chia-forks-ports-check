from json import load
from _base import std_names
from logging import getLogger

class pre_checks():

    _log: getLogger

    def __init__(self):
        super(pre_checks, self).__init__()

        final_verdict_helper = []
        for test in [self.check_input_json_integrity,
                     self.check_valid_filepaths]:
            final_verdict_helper += test()

        final_verdict = list(filter(lambda x: x['test'] == std_names.FAILED_TEST, final_verdict_helper))
        if len(final_verdict) > 0:
            self._log.error('Pre-checks failed. Cannot continue !')
            for message in final_verdict_helper:
                self._log.info(message['reason'])
            exit()
        self._log.info('Pre checks PASSED')

    def check_input_json_integrity(self):
        to_return = []
        return to_return if len(to_return) > 0 else [{'test': std_names.PASSED_TEST,
                                                      'reason': None}]

    def check_valid_filepaths(self):
        to_return = []
        return to_return if len(to_return) > 0 else [{'test': std_names.PASSED_TEST,
                                                      'reason': None}]
