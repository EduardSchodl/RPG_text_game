
from weapon import Weapon


class Character:
    """
       Třída Character charakterizuje postavy v RPG hře.

       @author Eduard Schödl
       @date 231116
    """

    HAND_LEFT: int = 0
    """
        Pomocná konstantna pro identifikaci levé ruky postavy.
    """
    HAND_RIGHT: int = 1
    """
        Pomocná konstantna pro identifikaci pravé ruky postavy.
    """

    def __init__(self, name: str, strength: int, agility: int, vitality: int):
        """
            Konstruktor třídy "Character". Vytvoří nový objekt typu Character.

            :param name: Jméno postavy
            :type name: str
            :param strength: Síla postavy
            :type strength: int
            :param agility: Hbitost postavy
            :type agility: int
            :param vitality: Zdraví postavy
            :type vitality: int
        """
        self.__right_hand_weapon = None
        self.__left_hand_weapon = None
        self.__name = name
        self.__strength = strength
        self.__agility = agility
        self.__vitality = vitality

    def __str__(self) -> str:
        """
            Metoda vrací formátovaný výpis postavy.
            Formát: name [vitality] (strength/agility)

            :return: Formátovaný řetězec
            :rtype: str
        """
        return f"{self.__name} [{self.__vitality}] ({self.__strength}/{self.__agility})"

    def attack(self) -> int:
        """
            Metoda vrací celkovou sílu postavy se započítanými zbraněmi.

            :return: Celková síla postavy
            :rtype: int
        """
        return self.__strength

    def defend(self, attack: int) -> int:
        """
            Tato metoda porovná celkovou vstupní sílu nepřítele a celkovou obrannou sílu postavy.
            V případě větší celkové síly útoku nepřítele než je celková obranná síla postavy
            ubere zdraví postavy o jejich rozdíl a vrátí ho, jinak vrací 0.

            :param attack: síla útoku nepřítele

            :return: Utrpěné poškození
            :rtype: int
        """
        if attack > self.__agility:
            diff: int = attack - self.__agility
            self.__vitality -= diff
            return diff
        else:
            return 0

    def is_alive(self) -> bool:
        """
            Metoda zjistí, jetli zdraví postavy je větší než 0. Tedy zda je živá.

            :return: Zda je postava živá
            :rtype: bool
        """
        return True if self.__vitality > 0 else False

    def take_weapon(self, weapon: Weapon, hand: int) -> bool:
        """
            Metoda se na základě parametru hand pokusí postavě vybavit zbraň do správné ruky.
            Jestli postava již v dané ruce zbraň má, vrátí False. Při úspěšném vybavení vrátí True.
            Po vybavení se k vlastnostem postavy přičte útočná a obranná síla zbraně.

            :param weapon: Objekt třídy Weapon
            :type weapon: Weapon
            :param hand: Identifikátor ruky do které zbraň vybavit
            :type hand: int

            :return: Zda si postava vybavila zbraň, nebo ne
            :rtype: bool
        """
        if hand == self.HAND_LEFT:
            if self.__left_hand_weapon:
                return False
            else:
                self.__left_hand_weapon = weapon

                if self.__left_hand_weapon is not None:
                    self.__strength += self.__left_hand_weapon.attack
                    self.__agility += self.__left_hand_weapon.defense

                return True
        else:
            if self.__right_hand_weapon:
                return False
            else:
                self.__right_hand_weapon = weapon

                if self.__right_hand_weapon is not None:
                    self.__strength += self.__right_hand_weapon.attack
                    self.__agility += self.__right_hand_weapon.defense

                return True
