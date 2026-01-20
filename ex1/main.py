def main() -> None:
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    print("\nDrawing and playing cards:")

if __name__ == "__main__":
    main()
"""
=== DataDeck Deck Builder ===

Building deck with different card types...
Deck stats: {'total_cards': 3, 'creatures': 1, 'spells': 1,
'artifacts': 1, 'avg_cost': 4.0}

Drawing and playing cards:

Drew: Lightning Bolt (Spell)
Play result: {'card_played': 'Lightning Bolt', 'mana_used': 3,
'effect': 'Deal 3 damage to target'}

Drew: Mana Crystal (Artifact)
Play result: {'card_played': 'Mana Crystal', 'mana_used': 2,
'effect': 'Permanent: +1 mana per turn'}

Drew: Fire Dragon (Creature)
Play result: {'card_played': 'Fire Dragon', 'mana_used': 5,
'effect': 'Creature summoned to battlefield'}

Polymorphism in action: Same interface, different card behaviors!
"""