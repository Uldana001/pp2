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
