from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUF = "debuf"


class SpellCard(Card):
    type: str = "Spell"

    def __init__(self, name: str, cost: int, rarity: str, effect_type: EffectType):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.consumed = False

    def play(self, game_state: dict) -> dict:
        if self.consumed:
            return {}
        self.consumed = True

    def resolve_effect(self, targets: list) -> dict:
        pass
