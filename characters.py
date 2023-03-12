from character import Character


class Characters:
    team: list[Character] = []
    def add(self, character: Character):
        self.team.append(character)
