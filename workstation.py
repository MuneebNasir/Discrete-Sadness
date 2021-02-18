from component import *
class Workstation:

    is_busy = False

    def __init__(self, buffer=None):
        self.buffer = buffer
        self.buffer2 = None


    def set_buffers(self, buffer2):
        self.buffer2 = buffer2

    
    def assemble_product(self):
        print(self.is_busy)
        # W1
        if self.buffer2 is None:
            if not is_buffer_empty('B1') and not self.is_busy:
                is_busy = True
                print(self.buffer.pop(0).name)
            else:
                print('Nothing to do here.')
        # 
        else:
            if not is_buffer_empty('B1') and not is_buffer_empty('B2'):
                # W2
                if self.buffer2[0].name == 'C2' and not self.is_busy:
                    is_busy = True
                    print(self.buffer.pop(0).name)
                    print(self.buffer2.pop(0).name)
                # W3
                elif self.buffer2[0].name == 'C3' and not self.is_busy :
                    is_busy = True
                    print(self.buffer.pop(0).name)
                    print(self.buffer2.pop(0).name)



    def is_buffer_free(self, buffer_type):
        if buffer_type == 'B1':
            return (len(self.buffer) > 0 and len(self.buffer) < 2)
        if buffer_type == 'B2':
            return (len(self.buffer2) > 0 and len(self.buffer2) < 2)
    
    
    def is_buffer_empty(self, buffer_type):
        if buffer_type == 'B1':
            return (len(self.buffer) == 0)
        if buffer_type == 'B2':
            return (len(self.buffer2) == 0)





