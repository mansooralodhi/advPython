

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


#----------Load Template-------------
template = env.get_template('4.customerName.jinja')

#----------Render Template-------------
customer = {"first_name": "John", "last_name": "Abraham"}
output = template.render(customer=customer)
print(output)

#----------Save Rendered Template---------------
# with open("renders/1.helloWorld.txt", 'w') as f:
#     print(output, file=f)
    
    
    