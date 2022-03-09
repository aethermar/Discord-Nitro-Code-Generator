import random
import string
import time
print('>_ NITRO CODE GENERATOR BY AETHERMAR (C72#3081)')
print('-----------------------------------------------------------------------------------')
print('')
v = input("Please enter the number of codes to generate: ")
x = 1
ERRORHAPPENED = 'False'

try: int(v)
except ValueError: 
    q = 3
    print('\nERROR: Please only enter numbers.\n')
    while q != 0:
        print('Closing in ' + str(q) + ' seconds.')
        time.sleep(1)
        q -= 1
        if q == 0: ERRORHAPPENED = 'True'
if ERRORHAPPENED == 'False':
    if int(v) <= 0:
        print('\nERROR: A number greater than 0 must be provided.\n')
        q = 3
        while q != 0:
            print('Closing in ' + str(q) + ' seconds.')
            time.sleep(1)
            q -= 1
            if q == 0: ERRORHAPPENED = 'True'


if ERRORHAPPENED == 'False':
    def nitro_generator(size=19, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    def ID_generator(size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    file_name = 'NitroGen Output #' + ID_generator() + '.txt'

    with open(file_name, 'a') as _c:
        while x <= int(v):
            content = 'https://discord.gift/' + nitro_generator()
            _c.write(content + '\n')
            x += 1
    print('\nSuccessfully generated ' + v + ' Nitro Codes. Output in ' + file_name)

    q = 3
    while q != 0:
        print('Closing in ' + str(q) + ' seconds.')
        time.sleep(1)
        q -= 1