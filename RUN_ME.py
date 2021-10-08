from _pitchfork import pitchfork
from threading import Thread
from time import sleep

if __name__ == '__main__':

    Thread(target=sleep, args=[99999]).start() # trick used to keep the window alive

    do = pitchfork()
    do.parse_all_cfgs()
    do.print_raw_parsed_data()
    do.print_port_conflicts()