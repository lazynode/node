import subprocess
import time


with subprocess.Popen(["./.node/neo-cli/bin/Release/net5.0/neo-cli"], stdin=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
    time.sleep(60)
    proc.communicate(b'exit\n', timeout=16)
