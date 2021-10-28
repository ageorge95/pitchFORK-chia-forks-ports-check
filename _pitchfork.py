from logging import getLogger
from concurrent.futures import ThreadPoolExecutor
from yaml import safe_load
from traceback import format_exc
from tabulate import tabulate
from os import system,\
    path
from shutil import copyfile
from datetime import datetime

from _pre_checks import pre_checks
from _base import configure_logger

class pitchfork(pre_checks):
    def __init__(self,
                 override_paths_list = None):
        configure_logger()
        self._log = getLogger(type(self).__name__)
        self.override_paths_list = override_paths_list

        system("color") # enable colored output in windows cmd

        super(pitchfork, self).__init__()

    def parse_cfg_slave(self,
                        valid_path):

        try:
            with open(valid_path, 'r') as yaml_in_handle:
                to_parse = safe_load(yaml_in_handle)
                network = 'mainnet' if 'mainnet' in to_parse['network_overrides']['config'].keys() else list(to_parse['network_overrides']['config'].keys())[0]
                to_return = {'nice_name': to_parse['network_overrides']['config'][network]['address_prefix'],
                             'daemon': {'port': to_parse['daemon_port']},
                             'farmer': {'port': to_parse['farmer']['port'],
                                        'rpc_port': to_parse['farmer']['rpc_port']},
                             'full_node': {'port': to_parse['full_node']['port'],
                                           'rpc_port': to_parse['full_node']['rpc_port']},
                             'harvester': {'port': to_parse['harvester']['port'],
                                           'rpc_port': to_parse['harvester']['rpc_port']},
                             'wallet': {'port': to_parse['wallet']['port'],
                                        'rpc_port': to_parse['wallet']['rpc_port']},
                             'config_path': valid_path}
                self._log.info('Successfully parsed {}'.format(valid_path))
                return to_return
        except:
            self._log.warning('Failed to parse {}'.format(valid_path))
            self._log.debug(format_exc(chain=False))

    def parse_all_cfgs(self):

        # parse the raw cfg
        self.contents = []
        with ThreadPoolExecutor(10) as exec_pool:
            for valid_path in self.input_paths_checked:
                self.contents.append(exec_pool.submit(self.parse_cfg_slave,(valid_path)).result())
            # remove contents for yaml files which have failed to be parsed
            self.contents = list(filter(lambda entry:entry != None, self.contents))

        # scan for port conlicts between the cfgs
        self.conflicts = []

        ports_with_conflicts = []  # use to filter out duplicate entries
        for key_1 in ['daemon', 'farmer', 'full_node', 'harvester', 'wallet']:
            for key_2 in ['daemon', 'farmer', 'full_node', 'harvester', 'wallet']:
                for variance_1 in ['port', 'rpc_port']:
                    for variance_2 in ['port', 'rpc_port']:

                        for coin_1 in self.contents:
                            coin1_nicename = coin_1['nice_name']
                            for coin_2 in self.contents:
                                coin2_nicename = coin_2['nice_name']
                                if coin1_nicename != coin2_nicename:

                                    subkey = '{}->{}'.format(coin1_nicename, coin2_nicename)
                                    if variance_1 in coin_1[key_1].keys() and variance_2 in coin_2[key_2].keys():
                                        port_left = coin_1[key_1][variance_1]
                                        port_right = coin_2[key_2][variance_2]

                                        if port_left == port_right and port_left not in ports_with_conflicts:
                                            ports_with_conflicts.append(port_left)
                                            self.conflicts.append({'conflict_pair': subkey,
                                                                  'conflict_left': '{}_{}'.format(key_1, variance_1),
                                                                  'conflict_right': '{}_{}'.format(key_2, variance_2),
                                                                  'conflict_port_left': coin_1[key_1][variance_1],
                                                                  'conflict_port_right': coin_2[key_2][variance_2],
                                                                  'config_path_left': coin_1['config_path'],
                                                                  'config_path_right': coin_2['config_path']})

    def print_raw_parsed_data(self):
        table = [[
                  entry['nice_name'],
                  entry['daemon']['port'],
                  entry['farmer']['port'],
                  entry['farmer']['rpc_port'],
                  entry['full_node']['port'],
                  entry['full_node']['rpc_port'],
                  entry['harvester']['port'],
                  entry['harvester']['rpc_port'],
                  entry['wallet']['port'],
                  entry['wallet']['rpc_port']
                  ] for entry in self.contents]
        self._log.info('Now printing ALL raw data:\n{}'.format(tabulate(table, ['Coin',
                                                                                'Daemon_port',
                                                                                'Farmer_port', 'Farmer_rpc_port',
                                                                                'FullNode_port', 'FullNode_rpc_port',
                                                                                'Harvester_port', 'Harvester_rpc_port',
                                                                                'Wallet_port', 'Wallet_rpc_port'], tablefmt="grid")))

    def print_port_conflicts(self):
        table = []
        if len(self.conflicts) > 0:
            table+=list([entry['conflict_pair'],
                         entry['conflict_left'],
                         entry['conflict_right'],
                         entry['conflict_port_left'],
                         entry['conflict_port_right']] for entry in self.conflicts)
        self._log.info('Now printing PORT CONFLICTS:\n{}'.format(tabulate(table, ['ConflictCoins',
                                                                                  'ConflictProcLeft',
                                                                                  'ConflictProcRight',
                                                                                  'ConflictPortLeft',
                                                                                  'ConflictPortRight'], tablefmt="grid")))
    def attempt_auto_fix(self,
                         override_confirmation = False):
        if len(self.conflicts) > 0:
            if (not override_confirmation and input('Do you want to attempt auto-ports-fix [Y/*]?').lower() == 'y') or override_confirmation:
                self._log.info('Auto-fix attempt in progress (left conflict will be resolved by default) ...')
                all_used_ports = [[
                                  entry['daemon']['port'],
                                  entry['farmer']['port'],
                                  entry['farmer']['rpc_port'],
                                  entry['full_node']['port'],
                                  entry['full_node']['rpc_port'],
                                  entry['harvester']['port'],
                                  entry['harvester']['rpc_port'],
                                  entry['wallet']['port'],
                                  entry['wallet']['rpc_port']
                                  ] for entry in self.contents]
                for conflict in self.conflicts:
                    self._log.info('Analyzing conflict: {} | {}->{} | {}'.format(conflict['conflict_pair'],
                                                                                conflict['conflict_left'],
                                                                                conflict['conflict_right'],
                                                                                conflict['conflict_port_left']))
                    new_port = conflict['conflict_port_left'] + 2
                    while new_port in all_used_ports:
                        new_port += 2
                    all_used_ports.append(new_port)

                    self._log.info('Decided to use the free port: {}'.format(new_port))

                    # make a backup
                    copyfile(conflict['config_path_left'],
                             path.join(path.dirname(conflict['config_path_left']), '{}_'.format(str(datetime.now()).replace(':', '_'))+path.basename(conflict['config_path_left'])))

                    # edit the cfg
                    with open(conflict['config_path_left'], 'r') as raw_file_in:
                        to_write = [line.replace(str(conflict['conflict_port_left']), str(new_port)) for line in raw_file_in.readlines()]

                    with open(conflict['config_path_left'], 'w') as raw_file_out:
                        raw_file_out.writelines(to_write)

                    self._log.info('Successfully resolved the conflict for {} | {}->{} | {}.'.format(conflict['conflict_pair'],
                                                                                                    conflict['conflict_left'],
                                                                                                    conflict['conflict_right'],
                                                                                                    conflict['conflict_port_left']))
                self._log.info('Please run the tool again to double check that the operation was successfull.')
            else:
                self._log.info('Auto-fix attempt aborted.')