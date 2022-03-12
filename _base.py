from logging import basicConfig,\
    INFO, DEBUG, WARNING, ERROR, CRITICAL,\
    Formatter,\
    StreamHandler, FileHandler
from sys import stdout

cfg_paths_template = [
                    r'{user_home}\.gold\mainnet\config\config.yaml',
                    r'{user_home}\.joker\mainnet\config\config.yaml',
                    r'{user_home}\.littlelambocoin\mainnet\config\config.yaml',
                    r'{user_home}\.bpx\mainnet\config\config.yaml',
                    r'{user_home}\.sit\mainnet\config\config.yaml',
                    r'{user_home}\.rolls\mainnet\config\config.yaml',
                    r'{user_home}\.ethgreen\mainnet\config\config.yaml',
                    r'{user_home}\.skynet\mainnet\config\config.yaml',
                    r'{user_home}\.venidium\mainnet\config\config.yaml',
                    r'{user_home}\.aedge\mainnet\config\config.yaml',
                    r'{user_home}\.chaingreen\mainnet\config\config.yaml',
                    r'{user_home}\.peas\mainnet\config\config.yaml',
                    r'{user_home}\.kujenga\mainnet\config\config.yaml',
                    r'{user_home}\.melon\mainnet\config\config.yaml',
                    r'{user_home}\.stai\mainnet\config\config.yaml',
                    r'{user_home}\.tranzact\mainnet\config\config.yaml',
                    r'{user_home}\.mogua\mainnet\config\config.yaml',
                    r'{user_home}\.mint\mainnet\config\config.yaml',
                    r'{user_home}\.salvia\mainnet\config\config.yaml',
                    r'{user_home}\.shibgreen\mainnet\config\config.yaml',
                    r'{user_home}\.olive\mainnet\config\config.yaml',
                    r'{user_home}\.btcgreen\mainnet\config\config.yaml',
                    r'{user_home}\.lucky\mainnet\config\config.yaml',
                    r'{user_home}\.chives\mainnet\config\config.yaml',
                    r'{user_home}\.chia\ext9\config\config.yaml',
                    r'{user_home}\.chia\mainnet\config\config.yaml',
                    r'{user_home}\.flax\mainnet\config\config.yaml',
                    r'{user_home}\.chiarose\mainnet\config\config.yaml',
                    r'{user_home}\.cryptodoge\mainnet\config\config.yaml',
                    r'{user_home}\.apple\mainnet\config\config.yaml',
                    r'{user_home}\.fork\mainnet\config\config.yaml',
                    r'{user_home}\.cannabis\mainnet\config\config.yaml',
                    r'{user_home}\.socks\mainnet\config\config.yaml',
                    r'{user_home}\.wheat\mainnet\config\config.yaml',
                    r'{user_home}\.melati\mainnet\config\config.yaml',
                    r'{user_home}\.taco\mainnet\config\config.yaml',
                    r'{user_home}\.greendoge\mainnet\config\config.yaml',
                    r'{user_home}\.tad\mainnet\config\config.yaml',
                    r'{user_home}\.covid\mainnet\config\config.yaml',
                    r'{user_home}\.avocado\mainnet\config\config.yaml',
                    r'{user_home}\.spare-blockchain\mainnet\config\config.yaml',
                    r'{user_home}\.lotus\mainnet\config/config.yaml',
                    r'{user_home}\.sector\mainnet\config/config.yaml',
                    r'{user_home}\.cactus\mainnet\config\config.yaml',
                    r'{user_home}\.flora\mainnet\config\config.yaml',
                    r'{user_home}\.kale\mainnet\config\config.yaml',
                    r'{user_home}\.maize\mainnet\config\config.yaml',
                    r'{user_home}\.hddcoin\mainnet\config\config.yaml',
                    r'{user_home}\.dogechia\mainnet\config\config.yaml',
                    r'{user_home}\.beernetwork\mainnet\config\config.yaml',
                    r'{user_home}\.pipscoin\mainnet\config\config.yaml',
                    r'{user_home}\.scam\mainnet\config\config.yaml',
                    r'{user_home}\.beet\mainnet\config\config.yaml',
                    r'{user_home}\.goldcoin\mainnet\config\config.yaml',
                    r'{user_home}\.kiwi\mainnet\config\config.yaml',
                    r'{user_home}\.xcha\mainnet\config\config.yaml',
                    r'{user_home}\.stor\mainnet\config\config.yaml'
                    ]

class std_names():
    FAILED_TEST = 'FAILED'
    PASSED_TEST = 'PASSED'

def configure_logger():
    class CustomFormatter(Formatter):
        grey = "\x1b[38;21m"
        yellow = "\x1b[33;21m"
        red = "\x1b[31;21m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        format = '%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d -> %(name)s - %(funcName)s] ___ %(message)s'

        FORMATS = {
            DEBUG: grey + format + reset,
            INFO: grey + format + reset,
            WARNING: yellow + format + reset,
            ERROR: red + format + reset,
            CRITICAL: bold_red + format + reset
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = Formatter(log_fmt)
            return formatter.format(record)

    ch = StreamHandler(stream=stdout)
    ch.setLevel(DEBUG)
    ch.setFormatter(CustomFormatter())
    fh = FileHandler("runtime_log.log")
    fh.setLevel(DEBUG)
    fh.setFormatter(Formatter('%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d -> %(name)s - %(funcName)s] ___ %(message)s'))

    basicConfig(datefmt='%Y-%m-%d:%H:%M:%S',
                level=INFO,
                handlers=[fh,ch])