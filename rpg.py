from __future__ import annotations

from character import Character
from weapon import Weapon


class RPG:
    """
        Třída RPG funguje jako prostředí pro běh hry.

        @Author: Eduard Schödl
        @Date: 231116
    """

    def input_character(self) -> Character:
        """
            Metoda postupně od uživatele načte všechny vlastnosti postavy a vytvoří nový objekt Character.

            :return: Objekt Character
            :rtype: Character
        """
        name = input("Jméno postavy: ")
        strength = int(input("Síla: "))
        agility = int(input("Hbitost: "))
        vitality = int(input("Zdraví: "))
        character: Character = Character(name, strength, agility, vitality)
        return character

    def input_weapon(self) -> Weapon | None:
        """
            Metoda postupně od uživatele načte všechny vlastnosti zbraně a vytvoří nový objekt Weapon.
            Postava nemusí mít zbraň. V tom případě vrací None.

            :return: Objekt Character nebo None
            :rtype: Character|None
        """
        name = input("Jméno zbraně: ")
        if name != "":
            strength = int(input("Útok: "))
            defense = int(input("Obrana: "))
            weapon: Weapon = Weapon(name, strength, defense)
            return weapon
        else:
            return None

    def equip_character(self, character: Character, left: Weapon | None, right: Weapon | None):
        """
            Metoda vybaví hráči případné zbraně do obou rukou.

            :param character: Postava, které se mají braně vybavit
            :type character: Character
            :param left: Zbraň do levé ruky
            :type left: Weapon
            :param right: Zbraň do pravé ruky
            :type right: Weapon
        """
        character.take_weapon(left, character.HAND_LEFT)
        character.take_weapon(right, character.HAND_RIGHT)

    def fight(self, character1: Character, character2: Character) -> Character:
        """
            Metoda spustí souboj mezi postavami. Začíná postava číslo 1 (vstupující do metody první).
            Po každém útoku se zkontroluje, zda postava číslo 2 (vstupující do metody druhá) přežila útok.
            Jestli postava přežila, souboj pokračuje. Jinak vrací přeživší postavu jako vítěze.

            :param character1: Postava číslo 1
            :type character1: Character
            :param character2: Postava číslo 2
            :type character2: Character
            :return: Vrací vítěze souboje
            :rtype: Character
        """
        attack = character1.attack()
        hit = character2.defend(attack)
        print(f"Útočí {character1} a dává {hit} zranění")

        if character2.is_alive():
            return self.fight(character2, character1)
        else:
            return character1

    def run(self):
        """
            Metoda spouští celou hru. Načte informace o postavě číslo 1 a jejích zbraních a vybaví ji.
            Poté ty samé informace načte o postavě číslo 2 a jejích zbraních a vybaví ji.
            Spustí souboj a vypíše jeho vítěze.
        """
        # ch1 = Character("Thorygg", 5, 3, 80)
        # w1 = Weapon("Tezky mec", 15, 2)
        # self.equip_character(ch1, w1, None)
        # ch2 = Character("vlk", 10, 10, 30)
        # winner = self.fight(ch1, ch2)
        # print(f"Vítěz: {winner}")

        character1 = self.input_character()
        weapon1 = self.input_weapon()
        weapon2 = self.input_weapon()
        self.equip_character(character1, weapon1, weapon2)

        character2 = self.input_character()
        weapon3 = self.input_weapon()
        weapon4 = self.input_weapon()
        self.equip_character(character2, weapon3, weapon4)

        winner = self.fight(character1, character2)
        print(f"Vítěz: {winner}")
