class GameObject:
    def __init__(self, object_id, name, x, y):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getX(self):
        return self._x

    def getY(self):
        return self._y


class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y)
        self._hp = hp

    def isAlive(self):
        return self._hp > 0

    def getHp(self):
        return self._hp

    def receiveDamage(self, damage):
        self._hp -= damage

        if self._hp < 0:
            self._hp = 0


class Building(GameObject):
    def __init__(self, object_id, name, x, y, built):
        super().__init__(object_id, name, x, y)
        self._built = built

    def isBuilt(self):
        return self._built


class Attacker:
    def attack(self, unit):
        raise NotImplementedError("El método attack debe ser implementado")


class Moveable:
    def move(self, x, y):
        raise NotImplementedError("El método move debe ser implementado")


class Archer(Unit, Attacker, Moveable):
    def __init__(self, object_id, name, x, y, hp, damage):
        super().__init__(object_id, name, x, y, hp)
        self._damage = damage

    def attack(self, unit):
        if self.isAlive() and unit.isAlive():
            unit.receiveDamage(self._damage)

    def move(self, x, y):
        if self.isAlive():
            self._x = x
            self._y = y


class Fort(Building, Attacker):
    def __init__(self, object_id, name, x, y, built, damage):
        super().__init__(object_id, name, x, y, built)
        self._damage = damage

    def attack(self, unit):
        if self.isBuilt() and unit.isAlive():
            unit.receiveDamage(self._damage)


class MobileHouse(Building, Moveable):
    def __init__(self, object_id, name, x, y, built):
        super().__init__(object_id, name, x, y, built)

    def move(self, x, y):
        if self.isBuilt():
            self._x = x
            self._y = y


if __name__ == "__main__":
    archer1 = Archer(1, "Robin", 0, 0, 100, 20)
    archer2 = Archer(2, "Enemy", 10, 10, 100, 15)

    print("HP del enemigo antes del ataque:", archer2.getHp())

    archer1.attack(archer2)

    print("HP del enemigo después del ataque:", archer2.getHp())

    archer1.move(5, 7)

    print("Nueva posición del arquero:", archer1.getX(), archer1.getY())

    fort = Fort(3, "Castle", 20, 20, True, 30)
    fort.attack(archer2)

    print("HP del enemigo después del ataque del fuerte:", archer2.getHp())

    house = MobileHouse(4, "Mobile House", 2, 3, True)
    house.move(8, 9)

    print("Nueva posición de la casa:", house.getX(), house.getY())