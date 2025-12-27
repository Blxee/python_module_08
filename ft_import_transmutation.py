"""
$> python3 ft_import_transmutation.py
=== Import Transmutation Mastery ===

Method 1 - Full module import:
alchemy.elements.create_fire(): Fire element created

Method 2 - Specific function import:
create_water(): Water element created

Method 3 - Aliased import:
heal(): Healing potion brewed with Fire element created and Water element created

Method 4 - Multiple imports:
create_earth(): Earth element created
create_fire(): Fire element created
strength_potion(): Strength potion brewed with Earth element created and Fire element created

All import transmutation methods mastered!
"""
print("Method 1 - Full module import:")
import alchemy.elements.create_fire
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
