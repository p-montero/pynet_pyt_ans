# includes the MyClass, MyChildClass Python classes
from mytest.simple import func1
from mytest.whatever import func2
from mytest.world import func3, MyClass, MyChildClass

__all__ = ('func1', 'func2', 'func3', 'MyClass', 'MyChildClass')
