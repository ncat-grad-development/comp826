# run_mininet_and_log.sh

#!/bin/bash

# Start Mininet and setup ARP poisoning, logging output to a file
python mininet_setup.py > attack_log.txt 2>&1

# Sleep for a while to let the ARP poisoning take effect
sleep 60

# Display the content of the log file
cat attack_log.txt

# End the script
exit 0
