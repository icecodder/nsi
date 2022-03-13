import re
import sys

#print(sys.argv)
ipc = sys.argv[1]

def ip_valide(ip):
  block = re.split(r"\.", ip)

  for e in block:
    e = int(e)
    
    if e >= 256:
      #print(f"{ip} n'est pas valide")
      return False

  if re.search(r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$", ip):
    #print(f"{ip} est valide")
    return True

  #print(f"{ip} n'est pas valide")
  return False

print(ip_valide(ipc))
