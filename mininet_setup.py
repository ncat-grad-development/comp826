# mininet_setup.py
from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.node import RemoteController

# Set up Mininet topology
topo = SingleSwitchTopo(3)
net = Mininet(topo=topo, controller=RemoteController)
net.start()

# Get hosts
h1, h2, h3 = net.get('h1'), net.get('h2'), net.get('h3')

# Get IP and MAC addresses
target_ip, target_mac = h2.IP(), h2.MAC()
source_ip = h1.IP()

# Start ARP poisoning attack from h3
h3.cmd('python arp_poison.py %s %s %s &' % (target_ip, target_mac, source_ip))

net.stop()
