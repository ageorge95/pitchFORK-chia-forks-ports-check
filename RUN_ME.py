from _base import configure_logger
from _pitchfork import pitchfork

if __name__ == '__main__':
    configure_logger()

    do = pitchfork()
    do.parse_all_cfgs()
    do.print_raw_parsed_data()