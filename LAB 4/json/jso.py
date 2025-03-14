import json

file_path = "/Users/uldanakonyratbaeva/Desktop/sample-data.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

interfaces = data["imdata"]

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else ""  # Description might be empty
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
"""
Interface Status
================================================================================
DN                                                 Description          Speed   MTU   
--------------------------------------------------------------------------------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/36]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/1]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/2]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/3]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/4]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/5]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/6]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/7]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/8]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/9]                               inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/10]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/11]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/12]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/13]                              inherit 9150  
topology/pod-1/node-201/sys/phys-[eth1/14]                              inherit 9150 
"""
