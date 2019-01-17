def method(self):
    return 1


klass = type('MyClass',(object,),{'method':method})
inst = klass()
print(inst.method())
print(type(inst))


class MetaClass(type):
    def __new__(mcs, name,bases,namespace):
        return super().__new__(mcs,name,bases,namespace)

    @classmethod
    def __prepare__(mcs, name, bases,**kwargs):
        return super().__prepare__(name,bases,**kwargs)

    def __init__(cls,name,bases,namespace,**kwargs):
        super().__init__(name,bases,namespace)

    def __call__(cls, *args, **kwargs):
        sd= super().__call__(*args,**kwargs)
        print(sd)
        return sd

Person = MetaClass('Person',(object,),{'method':method})
person = Person()
print(person.method())