# hello python program

def hello_func(text):
  '''returns text in a much more exiting way!'''
  return f'Hello {text.upper()}!!!!!!!'
  
#
# Main
#
if __name__ == "__main__":

  name = input('What is your name?  ')
  print(hello_func(name))
