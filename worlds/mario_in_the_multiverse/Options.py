from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, DeathLink, Range, Toggle, PerGameCommonOptions

class StarsToWin(Range):
    display_name = "Stars needed to get to Centrum Omnium"
    range_start = 1
    range_end = 123
    default = 70

class ItemLevels(Toggle):
    display_name = "Levels are Items"
    default = True

@dataclass
class MitmOptions(PerGameCommonOptions):
    stars_to_win: StarsToWin
    item_levels : ItemLevels
    death_link: DeathLink