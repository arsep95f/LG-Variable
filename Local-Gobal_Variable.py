g = "Global" 

def function():
 g = "Local" 
 print("Variable is " + g)

function()

print("Variable is " + g)