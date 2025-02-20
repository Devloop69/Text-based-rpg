import os, random, time, sys

# █ _

# Booleans!!!!!!

run = True;menu = True;play = False;rules = False;key = False;fight = False;standing = True;buy = False;speak = False;boss = False;ty = True;sell  = False;se = False

# Player Stats!!!!!

HP = 70
HPmax = HP
bars = 20
rsymbol = "█"
lsymbol = "░"
ps = "δ "
es = "[]"
cred = "\033[91m"
cyellow = "\33[93m"
cblue = "\33[34m"
cb = "\33[33m"
cgreen = "\033[92m"
cdefault = "\033[0m"
hc = cgreen
ATK = 6
pot = 1
elix = 0
gold = 0
x = 0
y = 0

ascii_art =[f"{cblue}Xx-----------------------------------------------------------------xX",
            f"{cblue}x {cb} ____                              _        ____                  {cblue}x",            
            f"{cblue}| {cb}|  _ \ _ __ __ _  __ _  ___  _ __ ( )___   / ___|__ ___   _____   {cblue}|",#type:ignore
            f"{cblue}| {cb}| | | | '__/ _` |/ _` |/ _ \| '_ \ \/ __| | |   / _` \ \ / / _ \  {cblue}|",#type:ignore
            f"{cblue}| {cb}| |_| | | | (_| | (_| | (_) | | | | \__ \ | |__| (_| |\ V /  __/  {cblue}|",#type:ignore
            f"{cblue}| {cb}|____/|_|  \__,_|\__, |\___/|_| |_| |___/  \____\__,_| \_/ \___|  {cblue}|",#type:ignore
            f"{cblue}x {cb}                 |___/                                            {cblue}x",
            f"Xx-----------------------------------------------------------------xX{cdefault}"]#type:ignore

#       x=0          x=1         x=2         x=3         x=4         x=5            x=6 
map = [["plains",    "plains",   "plains",   "plains",   "forest", "mountain",     "cave"], #y=0
       ["forest",    "forest",   "forest",   "forest",   "forest", "mountain",    "hills"], #y=1
       ["forest",     "field",   "bridge",   "plains",    "hills",   "forest",    "hills"], #y=2
       ["plains",      "shop",     "town",    "mayor",   "plains",    "hills", "mountain"], #y=3
       ["plains",     "field",    "field",   "plains",    "hills", "mountain", "mountain"]] #y=4

y_len = len(map)-1
x_len = len(map[0])-1

biome = {
   "plains":{
      "t": "PLAINS",
      "e": True},
   "forest":{
      "t": "WOODS",
      "e": True},
   "field":{
      "t": "FIELD",
      "e": False},
   "bridge":{
      "t": "BRIDGE",
      "e": True},
   "town":{
      "t": "TOWN CENTRE",
      "e": False},
   "shop":{
      "t": "SHOP",
      "e": False},
   "mayor":{
      "t": "MAYOR",
      "e": False},
   "cave":{
      "t": "CAVE",
      "e": False},
   "mountain":{
      "t": "MOUNTAIN",
      "e": True},
   "hills":{
      "t": "HILLS",
      "e": True},
}
e_list = ["Goblin","Witch","Slime"]
mobs = {
   "Goblin": {
      "hp": 35,
      "at": 3,
      "go": 12
   },
   "Witch": {
      "hp": 40,
      "at": 4,
      "go": 20
   },
   "Slime": {
      "hp": 15,
      "at": 1,
      "go": 7
   },
   "Dragon": {
      "hp": 150,
      "at": 12,
      "go": 105
   }
}
current_tile = map[y][x]
name_tile = biome[current_tile]["t"]
enemy_tile = biome[current_tile]["e"]

# Defines!!!!!!!
def printlist(art_list,delay):
   for row in art_list:
      print(row)
      time.sleep(delay)

def settings():
   global name,se
   while se:
      try:
         f = open("load.txt", "r")
         load_list = f.readlines()
         if len(load_list) == 9:
            name = load_list[0][:-1]
      except:
         print("No name available, start a new game!!")
         se = False
      clear()
      draw()
      print("Name: ",name)
      draw()
      print("1 - Change name")
      print("2 - Back")
      draw()
      choice = input("# ")

      if choice == '1':
         draw()
         name = input("What do you want your new name to be? ")
         save()
      elif choice == '2':
         save()
         se = False

def playerHP():
   global rbars,HP,HPmax,lbars,bars,rsymbol,lsymbol,cgreen,hc
   rbars = round(HP / HPmax * bars)
   lbars = bars - rbars
   print(f"|{hc}{rbars*rsymbol}"f"{lbars*lsymbol}{cdefault}|")
   if HP > 0.66 * HPmax:
      hc = cgreen
   elif HP > 0.33 * HPmax:
      hc = cyellow
   else:
      hc = cred

def potions():
   print(f"{cb}{pot*ps}{cdefault}")

def elixir():
   print(f"{cblue}{elix*es}{cdefault}")

def typewriter(text,delay):
   for char in text:
      print(char,end="")
      sys.stdout.flush()
      time.sleep(delay)

def clear():
   os.system("cls")

def drawty():
   dr = "Xx-----------------------------------------------------------------xX\n"
   typewriter(dr,0.000001)

def draw():
   print("Xx-----------------------------------------------------------------xX")

def save():
   list = [
    name,
    str(HP),
    str(ATK),
    str(pot),
    str(elix),
    str(gold),
    str(x),
    str(y),
    str(key)
   ]
   f = open("load.txt", "w")
   for item in list:
      f.write(item + "\n")
   f.close()

def heal(amount):
   global HP
   if HP + amount < HPmax:
      HP += amount
   else:
      HP = HPmax
   print(name + "`s HP refilled to " + str(HP) + "!")

def battle():
   save()
   global fight,play,run,HP,pot,elix,gold, boss,bars,rsymbol,lsymbol,key

   if not boss:
      enemy = random.choice(e_list)
   else:
      enemy = "Dragon"
   hp = mobs[enemy]["hp"]
   hpmax = hp
   at = mobs[enemy]["at"]
   go = mobs[enemy]["go"]
   while fight:
      erbars = round(hp / hpmax * bars)
      elbars = bars - erbars
      clear()
      draw()
      print("Defeat the "+enemy+"!")
      draw()
      print(enemy+"`s HP: "f"|{cred}{erbars*rsymbol}"f"{elbars*lsymbol}{cdefault}|")
      print(name+"`s HP: ",end="")
      playerHP()
      print("Potions: ",end="");potions()
      print("Elixir: ",end="");elixir()
      draw()
      print("1 - Attack")
      if pot > 0:
         print("2 - Use Potions (20 HP)")
      if elix > 0:
         print("3 - Use Elixir (40 HP)")
      print("4 - Escape")
      draw()
      choice = input("# ")
      if choice == "1":
         hp -= ATK
         print(name + " deals " + str(ATK) + " damage to the " + enemy + ".")
         if hp > 0:
            HP -= at
            print(enemy + " deals " + str(at) + " damage to " + name + ".")
         input("> ")
      elif choice == '2':
         if pot > 0:
            pot -= 1
            heal(20)
            print(enemy + " deals " + str(at) + " damage to " + name + ".")
         else:
            print("No Potion!")
         input("> ")
      elif choice == '3':
         if elix > 0:
            elix -= 1
            heal(40)
            print(enemy + " deals " + str(at) + " damage to " + name + ".")
         else:
            print("No Elixir!")
         input("> ")
      elif choice == '4':
         fight = False
         clear()
         draw()
         es = "You escaped the " + enemy
         typewriter(es,0.01)
         draw()
         input("> ")
         clear()
      
      if HP <= 0:
         draw()
         d = enemy + " defeated " + name + "....\n"
         typewriter(d,0.1)
         draw()
         fight = False
         play = False
         run = False
         g = "Game Over"
         dot = "....\n"
         typewriter(g,0.1)
         typewriter(dot,1)
         input("> ")
      if hp <= 0:
         draw()
         d = name + " defeated " + enemy + "!\n"
         typewriter(d,0.01)
         draw()
         fight = False
         gold += go
         g = "You`ve found " + str(go) + " gold!\n"
         typewriter(g,0.01)
         if random.randint(0,100) <= 25:
            pot += 1
            p = "You`ve found a potion!\n"
            typewriter(p,0.01)
         if random.randint(0,100) <= 15:
            elix += random.randint(1,3)
            el = "You`ve found some elixir!\n"
            typewriter(el,0.01)
         if enemy == "Dragon":
            drawty()
            c = "Congratulations!! You have finished the game!\n"
            typewriter(c,0.1)
            drawty()
            boss = False
            key = False
            play = False
            run = False
         input("> ")
         save()
         clear()

def shop():
   global buy,gold,pot,elix,ATK,HP,HPmax

   save()

   while buy:
      clear()
      g = "Not enough gold!\n"
      draw()
      print("Welcome to the shop!")
      draw()
      print("Gold: " + str(gold))
      print("Potions: ",end="");potions()
      print("Elixir: ",end="");elixir()
      print("ATK: " + str(ATK))
      print(f"HP: {HP} / {HPmax}")
      playerHP()
      draw()
      s = "1 - Buy Potion (20 HP) - 5 gold\n","2 - Buy Elixir (40 HP) - 8 gold\n","3 - Upgrade Weapon (+ 2 ATK) - 10 gold\n","4 - Upgrade Health (+ 10 HP) - 15 gold\n","5 - Sell\n","6 - Leave\n"
      typewriter(s,0.0001)
      draw()

      choice = input("# ")


      if choice == '1':
         if gold >= 5:
            pot += 1
            gold -= 5
            p = "You`ve bought a potion!\n"
            typewriter(p,0.01)
         else:
            typewriter(g,0.01)
         input("> ")
      elif choice == '2':
         if gold >= 8:
            elix += 1
            gold -= 8
            el = "You`ve bought an elixir point!\n"
            typewriter(el,0.01)
         else:
            typewriter(g,0.01)
         input("> ")
      elif choice == '3':
         if gold >= 10:
            ATK += 2
            if random.randint(0,100) <= 10:
               if gold >= 30:
                  gold -= random.randint(11,20)
                  s = "Shopkeeper scammed you!\n"
                  typewriter(s,0.01)
            else:
               gold -= 10
            s = "Your weapon is now stronger!\n"
            typewriter(s,0.01)
         else:
            typewriter(g,0.01)
         input("> ")
      elif choice == '4':
         if gold >= 15:
            gold -= 15
            HPmax += 10
            h = "Your HP is increased to " + str(HPmax) + "!\n"
            typewriter(h,0.01) 
         else:
            typewriter(g,0.01)
         input("> ")
      
      elif choice == '5':
         sell = True
         while sell:
            clear()
            draw()
            print("Welcome to the seller! what would you like to sell?")
            draw()
            sp = "1 - Sell Potion - 5 gold\n","2 - Sell Elixir - 7 gold\n","3 - Back\n"
            typewriter(sp,0.01)
            draw()
            choic = input("# ")

            if choic == '1':
               draw()
               if pot > 0:
                  gold += 5
                  pot -= 1
                  p = "You sold a potion!\n"
                  typewriter(p,0.01)
               else:
                  p = "No Potions!\n"
                  typewriter(p,0.01)
               draw()
            elif choic == '2':
               draw()
               if elix > 0:
                  gold += 7
                  elix -= 1
                  p = "You sold Elixir!\n"
                  typewriter(p,0.01)
               else:
                  p = "No Elixir!\n"
                  typewriter(p,0.01)
               draw()
            elif choic == '3':
               sell = False
            input("> ")
               
      
      elif choice == '6':
         save()
         buy = False

def mayor():
   global key, speak
   while speak:
      clear()
      draw()
      n = "Hello there " + name + "!\n"
      typewriter(n,0.0001)
      drawty()
      if ATK < 10 and HP <= 80:
         ns = "You`re not strong enough to face the Dragon yet, keep practicing and come back later!\n"
         typewriter(ns,0.0001)
         drawty()
         s = "You need more than 12 ATK and more than 80 HP\n"
         typewriter(s,0.0001)
         key = False
      else:
         d = "You might want to fight the Dragon now, take this key and be careful with the beast!\n"
         typewriter(d,0.0001)
         key = True
      draw()
      l = "1 - Leave\n"
      typewriter(l,0.0001)
      draw()
      choice = input("# ")

      if choice == '1':
         save()
         speak = False

def cave():
   global boss, key, fight

   while boss:
      clear()
      draw()
      print("Here lies the cave of the dragon...")
      print("What will you do?")
      draw()
      if key:
         print("1 - Use key")
      print("2 - Leave")
      choice = input("# ")
      if choice == '1':
         if key:
            fight = True
            battle()
      elif choice == '2':
         boss = False

# Main Loop!!!
while run:
    while menu:
        if ty:
         pr = 'Devaripsyou presents.....\n'
         typewriter(pr,0.1)
         time.sleep(1)
         clear()
         printlist(ascii_art,0.1)
         me = '1. New Game\n'
         lo = '2. Load Game\n'
         ru = '3. Rules\n'
         sett = '4. Settings\n'
         q = '5. Quit\n'
         typewriter(me,0.01)
         typewriter(lo,0.01)
         typewriter(ru,0.01)
         typewriter(sett,0.01)
         typewriter(q,0.01)
         drawty()

         if rules:
            clear()
            rul = 'Hi I am the creator and These are the rules:\n',"You would have to figure them out yourself.\n","I am just telling you that there are some theifs out there, watch out!\n"
            typewriter(rul,0.01)
            rules = False
            choice = ""
            input('> ')
         else:
               choice = input("# ")

         if choice == "1":
            clear()
            name = input('# Lets start, what`s your name? ')
            menu = False
            play = True
         elif choice == "2":
            try:
                  f = open("load.txt", "r")
                  load_list = f.readlines()
                  if len(load_list) == 9:
                     name = load_list[0][:-1]
                     HP = int(load_list[1][:-1])
                     ATK = int(load_list[2][:-1])
                     pot = int(load_list[3][:-1])
                     elix = int(load_list[4][:-1])
                     gold = int(load_list[5][:-1])
                     x = int(load_list[6][:-1])
                     y = int(load_list[7][:-1])
                     key = bool(load_list[8][:-1])
                  else:
                     s = "Save file is corrupted!\n"
                     typewriter(s,0.01)
                     input("> ")
            except OSError:
               s = "No loadable save file!\n"
               typewriter(s,0.01)
               input("> ")
            clear()
            n = "Welcome back " + name + "!\n"
            typewriter(n,0.01)
            input("> ")
            menu = False
            play = True
         elif choice == "3":
            rules = True
         elif choice == "4":
            se = True
            settings()
         elif choice == "5":
            quit()
         
         ty = False
        else:
            clear()
            printlist(ascii_art,0)
            draw()
            print('1. New Game')
            print('2. Load Game')
            print('3. Rules')
            print('4. Quit')
            draw()

            if rules:
               clear()
               rul = 'Hi I am the creator and These are the rules:\n',"You would have to figure them out yourself.\n","I am just telling you that there are some theifs out there, watch out!\n"
               typewriter(rul,0.01)
               rules = False
               choice = ""
               input('> ')
            else:
                  choice = input("# ")

            if choice == "1":
               clear()
               name = input('# Lets start, what`s your name? ')
               menu = False
               play = True
            elif choice == "2":
               try:
                     f = open("load.txt", "r")
                     load_list = f.readlines()
                     if len(load_list) == 9:
                        name = load_list[0][:-1]
                        HP = int(load_list[1][:-1])
                        ATK = int(load_list[2][:-1])
                        pot = int(load_list[3][:-1])
                        elix = int(load_list[4][:-1])
                        gold = int(load_list[5][:-1])
                        x = int(load_list[6][:-1])
                        y = int(load_list[7][:-1])
                        key = bool(load_list[8][:-1])
                     else:
                        s = "Save file is corrupted!\n"
                        typewriter(s,0.01)
                        input("> ")
               except OSError:
                  s = "No loadable save file!\n"
                  typewriter(s,0.01)
                  input("> ")
               clear()
               n = "Welcome back " + name + "!\n"
               typewriter(n,0.01)
               input("> ")
               menu = False
               play = True
            elif choice == "3":
               rules = True
            elif choice == "4":
               quit()
    while play:
      save()
      clear()

      if not standing:
         if biome[map[y][x]]["e"]:
            if random.randint(0,100) <= 30:
               fight = True
               battle()
      if play:
         draw()
         print("Location: " + biome[map[y][x]]["t"])
         draw()
         print("Name: " + name)
         print(f"HP: {HP} / {HPmax}")
         playerHP()
         print("ATK: " + str(ATK))
         print("Potions: ",end="");potions()
         print("Elixir: ",end="");elixir()
         print("Gold: " + str(gold))
         print("Coord: " + str(x),str(y))
         draw()
         print("0 - Save and Quit")
         if y > 0:
            n = "1 - North\n"
            typewriter(n,0.00001)
         if x < x_len:
            e = "2 - East\n"
            typewriter(e,0.00001)
         if y < y_len:
            s = "3 - South\n"
            typewriter(s,0.00001)
         if x > 0:
            w = "4 - West\n"
            typewriter(w,0.00001)
         if pot > 0:
            p = "5 - Use Potion (20 HP)\n"
            typewriter(p,0.00001)
         if elix > 0:
            el = "6 - Use Elixir (40 HP)\n"
            typewriter(el,0.00001)
         if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
               en = "7 - Enter\n"
               typewriter(en,0.00001)
         draw()

         dest = input('# ')

         if dest == '0':
            play = False
            menu = True
            save()
         elif dest == '1':
            if y > 0:
               y -= 1
               standing = False
         elif dest == '2':
            if x < x_len:
               x += 1
               standing = False
         elif dest == '3':
            if y < y_len:
               y += 1
               standing = False
         elif dest == '4':
            if x > 0:
               x -= 1
               standing = False
         elif dest == '5':
            if pot > 0:
               pot -= 1
               heal(30)
            else:
               p = "No Potions!"
               typewriter(p,0.01)
            input("> ")
            standing = True
         elif dest == '6':
            if elix > 0 :
               elix -= 1
               heal(40)
            else:
               el = "No Elixir!"
               typewriter(el,0.01)
            input("> ")
            standing = True
         elif dest == '7':
            if map[y][x] == "shop":
               buy = True
               shop()
            if map[y][x] == "mayor":
               speak = True
               mayor()
            if map[y][x] == "cave":
               boss = True
               cave()
         else:
            standing = True
