class Knight(object):

    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Knight"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return f'Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}'

class Archer(object):

    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Archer"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return f'Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}'


class Barracks(object):
    def generate_knight(self):
        return Knight(400, 5, 3, 1, "short sword")

    def generate_archer(self):
        return Archer(200, 7, 1, 5, "short bow")


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    archer1 = barracks.generate_archer()
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))
