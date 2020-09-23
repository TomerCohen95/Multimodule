# First Project (ModuleA)
class ModuleA:
  def __init__(module_b: ModuleB):
    print('im code from module A')
    module_b.hello()
    
  def hello():
    print('hello from A')
