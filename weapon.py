class Weapon:
    """
        Třída Weapon charakterizuje případné zbraně držené postavami.

        @author Eduard Schödl
        @date 231116
    """

    def __init__(self, name: str, attack: int, defense: int):
        """
            Konstruktor třídy "Weapon". Vytvoří nový objekt typu Weapon.

            :param name: Jméno zbraně
            :type name: str
            :param attack: Útočná síla zbraně
            :type attack: int
            :param defense: Obranná síla zbraně
            :type defense: int
        """
        self.__name = name
        self.__attack = attack
        self.__defense = defense

    def __str__(self) -> str:
        """
            Metoda vrací formátovaný výpis zbraně.
            Formát: name [attack/defense]

            :return: Formátovaný řetězec
            :rtype: str
        """
        return f"{self.__name} [{self.__attack}/{self.__defense}]"

    @property
    def attack(self) -> int:
        """
            Vrací útočnou sílu zbraně.

            :return: Útočná síla zbraně
            :rtype: int
        """
        return self.__attack

    @property
    def defense(self) -> int:
        """
            Vrací obrannou sílu zbraně.

            :return: Obranná síla zbraně
            :rtype: int
        """
        return self.__defense
