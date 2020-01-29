from common import AutoTest
import gc
for obj in gc.get_objects():
        print(type(obj))
        if isinstance(obj, AutoTest):
                print('yes')