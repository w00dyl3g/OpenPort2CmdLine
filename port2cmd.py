import os
import logging
import sys
import json

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

def printTable(record):    
    print("| PROCESS".ljust(20) + "| PID".ljust(20) + "| PROTO".ljust(20) + "| IFACE".ljust(20) + "| PORT".ljust(20) + "| CMDLINE")
    for _record in record:
        for value in _record.split(";")[:5]:
            print("| " + value[:18].ljust(18),end="")
        print("| " + _record.split(";SEP;")[1][:70],end="")
        print("")

def exportJSON(record):
    retJSON = [] 
    for _record in record:
        retJSON.append({
            'process': _record.split(";")[0],
            'PID': _record.split(";")[1],
            'PROTO': _record.split(";")[2],
            'IFACE': _record.split(";")[3],
            'PORT': _record.split(";")[4],
            'CMDLINE': _record.split(";SEP;")[1]
        })  
    
    with open('output.json', 'w') as fout:
        json.dump(retJSON, fout)

def cmdLine(pid):
    return os.popen('cat /proc/'+pid+'/cmdline').read()

def lsofParser():
    cmd = "lsof -i -n -P |awk 'NR > 1 {print $1\";\"$2\";\"$8\";\"$9}'"
    output = os.popen(cmd).readlines()
    record = []
    for line in output:
        pid = line.split(";")[1]
        record.append(line.replace("[::1]","127.0.0.1").replace(":",";").strip()+";SEP;"+cmdLine(pid).replace("\x00"," "))
    printTable(record)
    exportJSON(record)


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

