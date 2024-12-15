## IP
### 
###
###
### IPv6
#### PDU
#### extension headers-8octet*x
##### Fragmentation extension header
##### Routing extension header
#### Fragmentation and reassembly
#### minimum MTU-path MTU
#### path MTU discovery-ICMP
#### application
### SDN-gemeralized forwarding
#### match+action
#### OpenFlow abstration
### Middlebox
### Architecture
the goal is connectivity, the tool is the Internet Protocol, and the intelligence is end to end rather than hidden in the network.”
Three cornerstone beliefs:
simple connectivity
IP protocol: that narrow waist
intelligence, complexity at network edge
# U3 Control Plane
## intro 
### classification
## routing protocols
### link-state-OSPF
#### flooding
#### Dijikstra link-state routing algorithm
### distance-vector-RIP
#### Bellman-Ford algorithm
## IGP(intra-ISP routing) 
### RIP
distance metric: # of hops (max = 15 hops) 30s 25 subnets
### OSPF
园区网campus network
###  IS-IS
骨干网 backbone network; works on data link layer 
### EIGRP
## EGP(inter-ISP routing) 
### AS
### BGP
#### hot potato routing 
## SDN control plane
### SDN controller
interface layer to network /network-wide state /communication
### SDN network control apps
### OpenFlow--communication layer
## ICMP
## network management
### SNMP
### NETCONF

# U4 Transport Layer
## service 
## addressing 
IP+Port number
## socket Multiplexing/demultiplexing
## UDP 
### Header & CheckSum
## TCP & Principles of reliable data transfer 
### rdt 2.0 ARQ
### GBN & SR
## TCP
