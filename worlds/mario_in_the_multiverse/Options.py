from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, DeathLink, Range, Toggle, PerGameCommonOptions

class StarsToWin(Range):
    """
    Amount of Power Stars you need to obtain to access Centrum Omnium.
    """

    display_name = "Completion Stars"
    range_start = 1
    range_end = 123
    default = 80

class ItemLevels(Toggle):
    """
    Under normal circumstances, levels are accessed via power stars.
    This option instead removes the star requirement and adds levels to the item pool.
    Recommended for solo randomizers.
    """

    display_name = "Levels as Items"
    default = True

class Shopsanity(Toggle):
    """
    Shuffles the 5 shop items into the item pool.
    """

    display_name = "Shopsanity"
    default = True
class Keysanity(Toggle):
    """
    Shuffles Red Skull Key, Blue Skull Key, and Boat Key into the item pool.
    """

    display_name = "Keysanity"
    default = True

@dataclass
class MitmOptions(PerGameCommonOptions):
    stars_to_win: StarsToWin
    item_levels : ItemLevels
    shopsanity : Shopsanity
    keysanity : Keysanity
    death_link: DeathLink