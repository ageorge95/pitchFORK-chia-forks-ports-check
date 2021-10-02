from _pre_checks import pre_checks
from logging import getLogger
from concurrent.futures import ThreadPoolExecutor
from yaml import safe_load
from traceback import format_exc
from tabulate import tabulate

class pitchfork(pre_checks):
    def __init__(self):
        self._log = getLogger(type(self).__name__)

        super(pitchfork, self).__init__()

    def parse_cfg_slave(self,
                        valid_path):

        try:
            with open(valid_path, 'r') as yaml_in_handle:
                to_parse = safe_load(yaml_in_handle)
                to_return = {'nice_name': to_parse['network_overrides']['config']['mainnet']['address_prefix'],
                             'daemon': {'port': to_parse['daemon_port']},
                             'farmer': {'port': to_parse['farmer']['port']},
                             'full_node': {'port': to_parse['full_node']['port']},
                             'harvester': {'port': to_parse['harvester']['port']},
                             'wallet': {'port': to_parse['wallet']['port']}}
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
                self.contents.append(exec_pool.submit(self.parse_cfg_slave,(valid_path)).result())

    def print_raw_parsed_data(self):
        table = [[
                  entry['nice_name'],
                  entry['daemon']['port'],
                  entry['farmer']['port'],
                  entry['full_node']['port'],
                  entry['harvester']['port'],
                  entry['wallet']['port']
                  ] for entry in self.contents]
        self._log.info('Now printing ALL raw data:\n{}'.format(tabulate(table, ['Coin', 'Daemon_port', 'Farmer_port', 'FullNode_port', 'Harvester_port', 'Wallet_port'], tablefmt="grid")))

    def print_port_conflicts(self):
        conflicts = {}

        for key in ['daemon', 'farmer', 'full_node', 'harvester', 'wallet']:
            conflicts[key] = []
            generated_subkeys = []

            for coin_1 in self.contents:
                coin1_nicename = coin_1['nice_name']
                for coin_2 in self.contents:
                    coin2_nicename = coin_2['nice_name']
                    if coin1_nicename != coin2_nicename:
                        if coin_1[key]['port'] == coin_2[key]['port']:
                            subkey = '{}_{}'.format(coin1_nicename, coin2_nicename)
                            subkey_reverse = '{}_{}'.format(coin2_nicename, coin1_nicename)
                            if subkey_reverse not in generated_subkeys:
                                conflicts[key].append({'conflict_pair': subkey,
                                                       'conflict_port': coin_1[key]['port']})
                                generated_subkeys.append(subkey)

        table = []
        for key in ['daemon', 'farmer', 'full_node', 'harvester', 'wallet']:
            if len(conflicts[key]) > 0:
                table+=list([entry['conflict_pair'],
                              key,
                              entry['conflict_port']] for entry in conflicts[key])
        self._log.info('Now printing PORT CONFLICTS:\n{}'.format(tabulate(table, ['ConflictCoins', 'ConflictProcess', 'ConflictPort'], tablefmt="grid")))
