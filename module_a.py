from ModuleB.module_b import ModuleB


class ModuleA:
    def __init__(self, module_b: ModuleB):
        print('im code from module A')
        module_b.hello()

    def hello(self):
        print('hello from A')


ModuleA(ModuleB()).hello()
