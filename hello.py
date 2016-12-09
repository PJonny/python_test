Hex = ['E', 'C', 'C', 'B', '3', '5', '7', '9']

def Hextodec(hex_s):
    return list(str(int(''.join(hex_s), 16)))
if __name__ == "__main__":
    print Hextodec(Hex)

