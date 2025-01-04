

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


#----------Load Template-------------
template = env.get_template('1.helloWorld.jinja')

#----------Render Template-------------
output = template.render()
print(output)

#----------Save Rendered Template---------------
with open("renders/1.helloWorld.txt", 'w') as f:
    print(output, file=f)
    
    
    