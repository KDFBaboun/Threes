from ui.pygetch.getch.getch import *
import platform
def test_get_user_move():
        """
        Test de la fonction get_user_move
        """
        menu = [77, 109]
        quitter = [112,80]
        if platform.system() == "Linux":
                fleches = {27 : {91 : {65 : 'h', 66 : 'b', 67 : 'd', 68 : 'g'}}}
                print("get_user_move".center(32))
                print("Touches valides : ←, ↑, ↓, →, M")
                print("Appuyez sur [P] pour quitter")
                while True:
                        char = ord(getch())
                        print(char)
                        while True:
                            if char in quitter:
                                return False
                            elif char in menu:
                                print("La touche est valide")
                                break
                            elif char == 27:
                                char = ord(getch())
                                while True:
                                    if char in list(fleches[27]):
                                        char = ord(getch())
                                        if char in list(fleches[27][91]):
                                            print("La touche est valide")
                                            break
                                    else:
                                        print("Pas valide", char)
                                        break
                            elif char in list(fleches[27][91]) or char in (70, 51, 54, 53, 72, 50, 126, 80, 81, 82, 83, 49, 55, 56, 57, 48, 52, 112):
                                break
                            else:
                                print("La touche n'est pas valide", char)
                                break
        else:
                fleches = {0 : {72 : 'h', 75 : 'g', 77 : 'd', 80 : 'b'}}
                print("get_user_menu".center(32))
                print("Touches valides : ←, ↑, ↓, →, M")
                print("Appuyez sur [P] pour quitter")
                while True:
                        char = ord(getch())
                        if char in quitter:
                            return "Test de la fonction get_user_move : OK"
                        elif char in menu:
                            print("La touche est valide")
                        elif char in list(fleches):
                                char = ord(getch())
                                if char in list(fleches[0]):
                                        print("La touche est valide")
                        else:
                            print("La touche n'est pas valide.")
print(test_get_user_move())
