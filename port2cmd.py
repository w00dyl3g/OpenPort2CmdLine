import os
import logging
import sys

#### VAR ####
tools = [
    'lsof',
    'netstat',
    'ss'
]

funs = [
    'lsofParser',
    'netstatParser',
    'ssParser'
]

logLevels = [ 'd', 'i', 'w', 'e', 'c']
dictLevels = { 'd':10, 'i':20, 'w':30, 'e':40, 'c':50 }

### FUNCTIONS ###
def printBanner():
    print("OpenPort2CmdLine Linux Utility\n\n\
Set Logging Level\n\
  d: DEBUG\n\
  i: INFOTION\n\
  w: WARNING\n\
  e: ERROR\n\
  c: CRITICAL\n\n\
Example:\n\
  python3 port2cmd.py d (for debug purpose)")

def printTable(table):    
    print("| PROCESS".ljust(14) + "| PID".ljust(14) + "| PROTO".ljust(14) + "| IFACE".ljust(14) + "| PORT".ljust(14) + "| CMDLINE")
    for record in table:
        for value in record.split(";")[:-1]:
            print("| " + value[:12].ljust(12),end="")
        print("| " + record.split(";")[-1],end="")
        print("")

def cmdLine(pid):
    return os.popen('cat /proc/'+pid+'/cmdline').read()

def lsofParser():
    cmd = "lsof -i |awk 'NR > 1 {print $1\";\"$2\";\"$8\";\"$9}'"
    output = os.popen(cmd).readlines()
    table = []
    for line in output:
        pid = line.split(";")[1]
        table.append(line.replace(":",";").strip()+";"+cmdLine(pid).replace("\x00"," "))
    printTable(table)


### SETTING LOGGING LEVEL ###
if len(sys.argv) == 2:
    if sys.argv[1] in logLevels:
            logging.basicConfig(level=dictLevels[sys.argv[1]])
    else:
        printBanner()
        sys.exit(1)        
else:
    printBanner()
    sys.exit(1)


"""
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
"""

### CHECK PKGS INSTALLED ####
logging.info('Finding commons network utilities installed on the system...')

tools_count = 0
for tool in tools:
    if os.popen('which ' + tool).read() == "":
        logging.warning(tool + ' is missing on the system')
        tools.remove(tool)

if tools:
    logging.info('There are softwares for port inspection installed on the system:' + str(tools))
else:
    logging.error('There aren\'t softwares for port inspection installed on the system')
    sys.exit(1)      

### USING THE FIRST AVAILABLE NETTOOLS ###
tool = tools[0]
func = next(_func for _func in funs if tool in _func)
logging.debug('Using '+tool)
logging.debug('Calling '+func)

### STARTING PARSER
globals()[func]()

