"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    listita = [r, g, b]
    listita_2 = []
    for item in listita:
        if item > 255:
            listita_2.append(255)
        elif item < 0:
            listita_2.append(0)
        else:
            listita_2.append(item)
    r, g, b = listita_2[0], listita_2[1], listita_2[2]
    return str((f'{hex(r)}{hex(g)}{hex(b)}')).replace("x","")

print(rgb(1,2,3))