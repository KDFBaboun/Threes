from os import path
import sys
sys.path.append("../")
from ui.pygetch.getch.getch import *
from life_cycle.play import *

def test_get_user_menu():
    """
    Test de la fonction get_user_menu
    """
    acceptable = [110, 78, 76, 108, 115, 83, 99, 67, 113, 81]
    quitter = [112,80]
    print("get_user_menu".center(32))
    print("Touches valides : ")
    print("Appuyez sur [P] pour quitter")
    while True:
        char = ord(getch())
        while True:
            if char in quitter:
                return "Test de la fonction get_user_menu : OK"
            elif char in acceptable:
                print("La touche est valide")
                break
            elif char == 27:
                print("La touche n'est pas valide")
                break
            elif char == 91:
                ord(getch())
                break
            else:
                print("La touche n'est pas valide")
                break

def test_json() :
    """
    Test de fonction save_game et restore_game
    """
    partie = create_new_play()
    save_game(partie)
    partie2 = restore_game(partie)
    print(partie, partie2)
    assert partie["plateau"]['tiles'] == partie2["plateau"]['tiles']
    something = {}
    partie3 = restore_game(something)
    assert partie3["score"] == 3 and partie3["plateau"]["tiles"] != [0 for i in range(16)] and get_nb_empty_rooms(partie3['plateau']) == 14
    print("Test de la fonction save_game et restore_game : OK")

def test_create_new_play():
	"""
	Test de la fonction create_new_play
	"""
	partie = create_new_play()
	assert partie["score"] == 3 and partie["plateau"]["tiles"] != [0 for i in range(16)]
	assert get_value(partie['plateau'], partie['next-tile']["0"]["lig"], partie['next-tile']["0"]["col"]) == partie['next-tile']["0"]["val"] and get_value(partie['plateau'], partie['next-tile']["1"]["lig"], partie['next-tile']["1"]["col"]) == partie['next-tile']["1"]["val"]
	print('Test de la fonction create_new_play : OK')

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
                        if char in quitter:
                        	break
                        elif char in menu:
                                print("La touche est valide")
                        elif char in list(fleches):
                                char = ord(getch())
                                if char in list(fleches[27]):
                                        char = ord(getch())
                                        if char in list(fleches[27][91]):
                                                print("La touche est valide")
                                else:
                                    print("test")
                        else:
                            print("La touche n'est pas valide")
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
