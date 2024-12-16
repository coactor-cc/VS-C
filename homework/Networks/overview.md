# U1 Intro
## What is Internet?What is a protocol?
### Internet Architecture Management
### Domain Name Management
### Internet Standards
#### RFC
#### IETF

## Network Edge 
### host
### Access networks
#### access approach
#### home networks
#### wireless networks
### Physical Media
#### Links
#### simplex&duplex
## Network Core
### packet/circuit switching
### Internet Structure
## Performance
### loss
### delay
### throughput
## Secuirity
## Layer
## History
# U2 Network Layer:data plane
## overview 
## whats inside a router
### input ports 
### switching fabric
### output ports
## IP
### datagram format 
### Addressing
#### Subnet  
#### CIDR
无类别域间路由
#### DHCP
### NAT (networks address translation)
### IPv6
#### PDU
#### extension headers-8octet*x
##### Fragmentation extension header
##### Routing extension header
#### Fragmentation and reassembly
#### minimum MTU-path MTU
#### path MTU discovery-ICMP
#### application
## SDN-gemeralized forwarding
### match+action
### OpenFlow abstration
## Middlebox
## Architecture
the goal is connectivity, the tool is the Internet Protocol, and the intelligence is end to end rather than hidden in the network.”
Three cornerstone beliefs:
simple connectivity
IP protocol: that narrow waist
intelligence, complexity at network edge
# U3 Network Layer:Control Plane
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
## overview
### service 
### addressing 
IP+Port number
### socket Multiplexing/demultiplexing
## UDP 
### Header & CheckSum
##  Principles of reliable data transfer 
### rdt 2.0 ARQ
### GBN & SR
## TCP
### Shake hands
### Close connection
### Flow control 
### Congestion control 

# U5 Link layer
## intro 
broadcast(Ethernet、WLAN) or PPP    
### service
#### framing 
#### reliable delivery
#### error detection
## Multiple access links & protocol
### CSMA/CD
### CSMA/CA
## LANS
### Ethernet  
### switches
#### STP
### VLANs
## link virtualization:MPLS
## VPN

# U6 Wireless & Mobile
## overview
## wireless LAN
### 802.11
### 802.11ac
### 802.11ax
## cellular networks
### 3GPP
### 5G
## mobile IP
## wireless mesh networks
