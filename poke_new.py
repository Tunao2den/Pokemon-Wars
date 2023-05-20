class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def createpokelist():
        poke1 = Pokemon("Bulbasaur", "grass")
        poke2 = Pokemon("Venusaur", "grass")
        poke3 = Pokemon("Squirtle", "water")
        poke4 = Pokemon("Wartortle", "water")
        poke5 = Pokemon("Charmeleon", "fire")
        poke6 = Pokemon("Charizard", "fire")
        return [poke1, poke2, poke3, poke4, poke5, poke6]


class Battle:
    def __init__(self):
        self.pokemons = Pokemon.createpokelist()
        self.poke_attack = None
        self.poke_defence = None

    def get_user_input(self):
        print("Available Pokemons: ")
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i+1}. {pokemon.name} - Type: {pokemon.type}")

        attack_poke_index = (int(input("Enter the corresponding number for attacking Pokemon: "))-1)
        defend_poke_index = (int(input("Enter the corresponding number for defending Pokemon: "))-1)

        if (
            attack_poke_index < 0
            or attack_poke_index >= len(self.pokemons)
            or defend_poke_index < 0
            or defend_poke_index >= len(self.pokemons)
        ):
            print("Please enter a valid number! ")
            return

        self.poke_attack = self.pokemons[attack_poke_index]
        self.poke_defence = self.pokemons[defend_poke_index]
        print(f"{self.poke_attack.name}" + " vs. " + f"{self.poke_defence.name}")
        print("Fight...")
    def logic(self):
        type_indexer = {0: "grass", 1: "water", 2: "fire"}
        queue_map = [[0, 1, -1], # grass 
                     [-1, 0, 1], # water
                     [1, -1, 0]] # fire    
        result_dict = {-1: "lose", 0: "tie", 1: "win"}
        for key, values in type_indexer.items():
            if values == self.poke_attack.type:
                attack_queue_map = key
            if values == self.poke_defence.type:
                defence_queue_map = key
        result_value = queue_map[attack_queue_map][defence_queue_map]
        for key, values in result_dict.items():
            if key == result_value:
                result = values
        return result

    def run_battle(self):
        self.get_user_input()
        res = self.logic()
        if res == "lose":
            print(f"The winner is {self.poke_defence.name}!")
        elif res == "tie":
            print("Tie!")
        elif res == "win":
            print(f"The winner is {self.poke_attack.name}!")

def main():
    battle = Battle()
    battle.run_battle()

if __name__ == "__main__":
    main()