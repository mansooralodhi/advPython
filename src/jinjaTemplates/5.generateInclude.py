

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

#----------Load Template-------------
template = env.get_template('5.includes.jinja')

#----------Render Template-------------
bus_class_data = {"Class": "CAN", "prefix": "icd1_"}
output = template.render(bus_class_data = bus_class_data)
print(output)

#----------Save Rendered Template---------------
with open("renders/5.includes.txt", 'w') as f:
    print(output, file=f)
    
    
    