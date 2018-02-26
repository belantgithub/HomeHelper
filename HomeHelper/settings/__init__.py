try:
    from HomeHelper.settings.local import *
except ImportError:
    raise Exception('Please create local.py file, you can use local_example.py')