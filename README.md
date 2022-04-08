<h1>OpenPort2CmdLine Linux Utility<br /></h1>

<h2>Set Logging Level<br /></h2>
  d: DEBUG<br />
  i: INFOTION<br />
  w: WARNING<br />
  e: ERROR<br />
  c: CRITICAL<br /><br />

<h2>Example:</h2><br />
  python3 port2cmd.py d (for debug purpose)<br /><br />

<h2>Output:</h2>
<code>
[{"process": "nc", "PID": "1153", "PROTO": "TCP", "IFACE": "*", "PORT": "9999", "CMDLINE": "nc -lnvp 9999 "}, {"process": "nc", "PID": "2372", "PROTO": "TCP", "IFACE": "*", "PORT": "19999", "CMDLINE": "nc -lnvp 19999 "}, {"process": "python3", "PID": "2376", "PROTO": "TCP", "IFACE": "*", "PORT": "8000", "CMDLINE": "python3 -m http.server "}]
</code>
