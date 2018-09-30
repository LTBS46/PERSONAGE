import MAIN

def interpret(r_input):
    if r_input == ("close" or "exit"):
        print("OK")
        exit()
    elif r_input == "present":
        MAIN.PJ.present()
        print("OK")
    elif r_input == "attaque":
        MAIN.PJ.attack()
        MAIN.your_turn = False
    elif str.startswith(r_input, "take_a "):
        g_max = int(str.strip(r_input, "take_a "))
        g = 0
        while g <= g_max:
            MAIN.mob.attack()
            g += 1
    else:
        print("huh?")
