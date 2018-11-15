
BUFFERSIZE = 4096

lex_buffer_1 = '\0' * BUFFERSIZE
lex_buffer_1_start=0
lex_buffer_1_forward=0

lex_bufffer_2 = '\0' * BUFFERSIZE
lex_buffer_2_start=0
lex_buffer_2_forward=0

path='FileGen 1MB.txt'


def loadBuffer2(buffer):
    with open(path, 'r') as f:
        while True:
            lex_buffer_1 = f.read(4096)
            if not lex_buffer_1:
                break

            print('\n\n\n\n\n')                
            print('#################################################################################')
            print(lex_buffer_1)  



def loadBuffer1(buffer):
    with open(path, 'rb') as f:
        count=0
        for lex_buffer_1 in iter(lambda: f.read(4096), b''):
            count +=1
            print('\n\n\n\n\n')
            print('#################################################################################')
            print(lex_buffer_1)
        print(f'Number of iterations {count}')


def start():

    loadBuffer1(lex_buffer_1)
   # loadBuffer2(lex_buffer_2)

if __name__ == '__main__':
    start()