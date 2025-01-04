

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

#----------Load Template-------------
template = env.get_template('2.helloName.jinja')

#----------Render Template-------------

output = template.render(name= "Mansoor")
print(output)

    
    
    