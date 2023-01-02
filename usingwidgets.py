import ipywidgets as widgets
from IPython.display import display

age=widgets.IntText(description="Alter:", value=25)
display(age)

print(age.value)

button = widgets.Button(description="OK")
display(button)

def on_button_click(p):
  print("on_button_click()")
  
button.on_click(on_button_click)

# Aufgabe

