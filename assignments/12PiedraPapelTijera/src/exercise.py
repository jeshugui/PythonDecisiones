def main():
    # Escribe tu código abajo de esta línea
    tA = str(input('Tirada de Ana: '))
    tJ = str(input('Tirada de Juan: '))
    
    if len(tA)!= 1 or len(tJ) != 1:
        print ("Las tiradas deben ser un carácter")
    elif tA == str('a') and tJ == str('t'):
        print('Gana Ana')
    elif tA == str('a') and tJ == str('p'):
        print('Gana Juan')
    elif tA == str('a') and tJ == str('a'):
        print('Empate')
    elif tA == str('t') and tJ == str('p'):
        print('Gana Ana')
    elif tA == str('t') and tJ == str('t'):
        print('Empate')
    elif tA == str('p') and tJ == str('p'):
        print('Empate')
    elif tA == str('p') and tJ == str('a'):
        print('Gana Ana')
    elif tA == str('t') and tJ == str('a'):
        print('Gana Juan')
    elif tA == str('p') and tJ == str('t'):
        print('Gana Juan')
    else:
        print('Tirada incorrecta')

if __name__ == '__main__':
    main()
