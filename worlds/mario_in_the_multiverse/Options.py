from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, DeathLink, Range, Toggle, PerGameCommonOptions

class StarsToWin(Range):
    display_name = "Stars needed to get to Centrum Omnium"
    range_start = 1
    range_end = 123
    default = 80

class ItemLevels(Toggle):
    display_name = "Levels are Items"
    default = True

class Shopsanity(Toggle):
    display_name = "Shopsanity"
    default = True
class Keysanity(Toggle):
    display_name = "Keysanity"
    default = True

@dataclass
class MitmOptions(PerGameCommonOptions):
    stars_to_win: StarsToWin
    item_levels : ItemLevels
    shopsanity : Shopsanity
    keysanity : Keysanity
    death_link: DeathLink