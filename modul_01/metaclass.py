
class Meta(type):
    instance_created = 0

    def __new__(mcs, name, bases, namespace, **kwargs):
        instance = super().__new__(mcs, name, bases, namespace)
        instance.class_number = mcs.instance_created
        mcs.instance_created += 1
        return instance

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


print(Cls1.class_number, Cls2.class_number)
#assert (Cls1.class_number, Cls2.class_number) == (0, 1)
print('-------------------')

a, b = Cls1(''), Cls2('')

print(a.class_number, b.class_number)
#assert (a.class_number, b.class_number) == (0, 1)