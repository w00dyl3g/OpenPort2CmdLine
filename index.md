## OpenPort2CmdLine Linux Utility

### Parameters:
```markdown
  d: DEBUG
  i: INFOTION
  w: WARNING
  e: ERROR
  c: CRITICAL
```

### Example
```
  python3 port2cmd.py d (for debug purpose)
```

### Output (with | jq)
```
[
    {
        "process": "nc", 
        "PID": "1153", 
        "PROTO": "TCP", 
        "IFACE": "*", 
        "PORT": "9999", 
        "CMDLINE": "nc -lnvp 9999 "
    }, 
    {
        "process": "nc", 
        "PID": "2372", 
        "PROTO": "TCP", 
        "IFACE": "*", 
        "PORT": "19999", 
        "CMDLINE": "nc -lnvp 19999 "
    }, 
    {
        "process": "python3", 
        "PID": "2376", 
        "PROTO": "TCP", 
        "IFACE": "*", 
        "PORT": "8000", 
        "CMDLINE": "python3 -m http.server "
    }
]
```


