import sys

spec_replacement=str(open("RUN_ME.spec", "r").readlines()).replace(r'name=''\'pitchfork_dev\'''', r'name=''\'{}\''''.format(sys.argv[-1]))
open("RUN_ME.spec", "w").writelines(eval(spec_replacement))