import yaml
import os
import glob
directory = "/opt/test/"
t_memory = 0
t_cpu = 0

files = glob.glob(directory + '/**/deployment.yaml', recursive=True)

if not files:
  print("No files found")

for filename in files:
    if filename.endswith(".yaml"): 
        print(filename)
        with open(filename, "r") as stream:
          try:
            data = yaml.safe_load(stream)
            #Memory
            try:
              memory = data['spec']['template']['spec']['containers'][0]['resources']['limits']['memory']
            except:
              memory = "0Mi"    
            try:
              cpu = data['spec']['template']['spec']['containers'][0]['resources']['limits']['cpu']
            except:
              cpu = 0   
            #memory   
            c_memory = int(memory.split('Mi')[0])
            t_memory = t_memory + c_memory
            #CPU
            c_cpu = int(cpu)
            t_cpu = t_cpu + c_cpu

          except yaml.YAMLError as exc:
            print(exc)
            continue
    else: 
        continue
print("[INFO] MEMORY in Mi")
print(t_memory)
print("[INFO] CPU")
print(t_cpu)
