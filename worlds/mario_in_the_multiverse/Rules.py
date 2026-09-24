from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .Global import LevelList

if TYPE_CHECKING:
    from .World import MitmWorld

def set_all_rules(world: MitmWorld) -> None:
    # Ability Rules
    world.set_rule(world.get_location("Bubble Hat"), Has("Cutter"))
    world.set_rule(world.get_location("Gadget Watch"), Has("Shock Rocket"))
    world.set_rule(world.get_location("Esteemed Mortal"), Has("Pizza Knight"))

    # Level Entrance Rules
    for level in LevelList:
        world.set_rule( world.get_entrance(level + " Entrance"), Has(level)  )

    # Super Star Ultra
    world.set_rule(world.get_location("Super Star Ultra Star 4"), Has("Cutter"))
    world.set_rule(world.get_location("Super Star Ultra Star 6"), Has("Phasewalk"))
    world.set_rule(world.get_location("Super Star Ultra Star 7"), Has("Shock Rocket"))
    world.set_rule(world.get_location("Super Star Ultra Star 8"), Has("Gadget Watch"))

    # Mario in Bikini Bottom
    world.set_rule(world.get_location(
        "Mario in Bikini Bottom Star 2"),
        HasAll("Cutter", "Bubble Hat"),
    )
    world.set_rule(world.get_location("Mario in Bikini Bottom Star 4"), Has("Bubble Hat"))
    world.set_rule(world.get_location("Mario in Bikini Bottom Star 5"), Has("Helmet & Drill"))
    world.set_rule(world.get_location("Mario in Bikini Bottom Star 6"), Has("Pizza Knight"))
    world.set_rule(world.get_location("Mario in Bikini Bottom Star 7"), Has("Phasewalk"))

    # Piranha Pit
    world.set_rule(world.get_location("Piranha Pit Star 1"), Has("Inkling"))
    world.set_rule(world.get_location("Piranha Pit Star 3"), Has("Inkling"))
    world.set_rule(world.get_location("Piranha Pit Star 4"), Has("Bubble Hat"))
    world.set_rule(world.get_location("Piranha Pit Star 6"), Has("Shock Rocket"))
    world.set_rule(world.get_location("Piranha Pit Star 7"), Has("Helmet & Drill"))

    # Mario Mushroom Havoc
    world.set_rule(world.get_location("Mario Mushroom Havoc Star 1"), Has("Shock Rocket"))
    world.set_rule(world.get_location("Mario Mushroom Havoc Star 2"), Has("Shock Rocket"))
    world.set_rule(world.get_location("Mario Mushroom Havoc Star 3"), Has("Shock Rocket"))
    world.set_rule(world.get_location(
        "Mario Mushroom Havoc Star 4"),
        HasAll("Shock Rocket", "Gadget Watch", "Helmet & Drill"),
    )
    world.set_rule(world.get_location("Mario Mushroom Havoc Star 5"), Has("Cutter") & Has("Shock Rocket"))
    world.set_rule(world.get_location("Mario Mushroom Havoc Star 6"), Has("Aku Aku") & Has("Shock Rocket"))
    world.set_rule(world.get_location("Mario Mushroom Havoc Star 8"), Has("Shock Rocket"))

    # Opportunity
    world.set_rule(world.get_location("Opportunity Star 1"), Has("Phasewalk"))
    world.set_rule(world.get_location("Opportunity Star 3"), Has("HM Fly"))
    world.set_rule(world.get_location("Opportunity Star 4"), Has("HM Fly"))
    world.set_rule(world.get_location("Opportunity Star 6"), Has("HM Fly"))
    world.set_rule(world.get_location("Opportunity Star 7"), Has("Doom Shotgun"))

    # Bioshock Rapture
    world.set_rule(world.get_location("Bioshock Rapture Star 3"), Has("Helmet & Drill"))
    world.set_rule(world.get_location(
        "Bioshock Rapture Star 4"),
        HasAll("Helmet & Drill", "Shock Rocket", "Phasewalk"),
    )
    world.set_rule(world.get_location(
        "Bioshock Rapture Star 5"),
        HasAll("Helmet & Drill", "Phasewalk", "Inkling"),
    )
    world.set_rule(world.get_location("Bioshock Rapture Star 6"), Has("Helmet & Drill"))
    world.set_rule(world.get_location("Bioshock Rapture Star 7"), Has("Helmet & Drill"))

    # Beyond the Cursed Pizza
    world.set_rule(world.get_location("Beyond the Cursed Pizza Star 2"), Has("Pizza Knight"))
    world.set_rule(world.get_location(
        "Beyond the Cursed Pizza Star 3"),
        HasAll("Pizza Knight", "HM Fly"),
    )
    world.set_rule(world.get_location("Beyond the Cursed Pizza Star 4"), Has("Pizza Knight"))
    world.set_rule(world.get_location(
        "Beyond the Cursed Pizza Star 5"),
        HasAll("Pizza Knight", "Dash Booster"),
    )
    world.set_rule(world.get_location("Beyond the Cursed Pizza Star 6"), Has("Pizza Knight"))
    world.set_rule(world.get_location(
        "Beyond the Cursed Pizza Star 8"),
        HasAll("Pizza Knight", "Dash Booster"),
    )

    # Mario New Mecca
    # "Chronos" intentionally matches ITEM_NAME_TO_ID as supplied.
    world.set_rule(world.get_location("Mario New Mecca Star 1"), Has("Chronos"))
    world.set_rule(world.get_location("Mario New Mecca Star 2"), Has("Pizza Knight") & Has("Chronos"))
    world.set_rule(world.get_location("Mario New Mecca Star 3"), Has("Chronos"))
    world.set_rule(world.get_location("Mario New Mecca Star 4"), Has("Shock Rocket") & Has("Chronos"))
    world.set_rule(world.get_location("Mario New Mecca Star 5"), Has("Chronos"))
    world.set_rule(world.get_location("Mario New Mecca Star 6"), Has("Chronos"))
    world.set_rule(world.get_location("Mario New Mecca Star 7"), Has("Phasewalk") & Has("Chronos"))

    # DOOM
    world.set_rule(world.get_location("DOOM Star 1"), Has("Doom Shotgun"))
    world.set_rule(world.get_location("DOOM Star 2"), Has("Doom Shotgun"))
    world.set_rule(world.get_location("DOOM Star 3"), Has("Doom Shotgun"))
    world.set_rule(world.get_location("DOOM Star 4"), Has("Doom Shotgun"))
    world.set_rule(world.get_location(
        "DOOM Star 6"),
        HasAll("Doom Shotgun", "Inkling"),
    )
    world.set_rule(world.get_location("DOOM Star 8"), Has("Doom Shotgun"))

    # From Russia With Love
    world.set_rule(world.get_location(
        "From Russia With Love Star 1"),
        HasAll("Shock Rocket", "Gadget Watch"),
    )
    world.set_rule(world.get_location(
        "From Russia With Love Star 2"),
        HasAll("Gadget Watch", "Doom Shotgun", "Phasewalk"),
    )
    world.set_rule(world.get_location(
        "From Russia With Love Star 3"),
        HasAll("Doom Shotgun", "Gadget Watch"),
    )
    world.set_rule(world.get_location("From Russia With Love Star 4"), Has("Gadget Watch"))
    world.set_rule(world.get_location(
        "From Russia With Love Star 6"),
        HasAll("Gadget Watch", "Inkling"),
    )
    world.set_rule(world.get_location(
        "From Russia With Love Star 8"),
        HasAll("Gadget Watch", "Shock Rocket"),
    )

    # Eucreteak City
    world.set_rule(world.get_location("Eucreteak City Star 1"), Has("HM Fly"))
    world.set_rule(world.get_location("Eucreteak City Star 1"), Has("Inkling"))
    world.set_rule(world.get_location(
        "Eucreteak City Star 3"),
        HasAll("Pizza Knight", "HM Fly", "Chronos"),
    )
    world.set_rule(world.get_location(
        "Eucreteak City Star 4"),
        HasAll("Helmet & Drill", "Pizza Knight"),
    )
    world.set_rule(world.get_location("Eucreteak City Star 5"), Has("HM Fly"))
    world.set_rule(world.get_location("Eucreteak City Star 6"), Has("Shock Rocket"))
    world.set_rule(world.get_location(
        "Eucreteak City Star 7"),
        HasAll("Gadget Watch", "HM Fly"),
    )
    world.set_rule(world.get_location("Eucreteak City Star 8"), Has("HM Fly"))

    # N-Sanity Island
    world.set_rule(world.get_location("N-Sanity Island Star 1"), Has("Aku Aku"))
    world.set_rule(world.get_location("N-Sanity Island Star 4"), Has("HM Fly"))
    world.set_rule(world.get_location("N-Sanity Island Star 5"), Has("Helmet & Drill"))
    world.set_rule(world.get_location(
        "N-Sanity Island Star 6"),
        HasAll("Doom Shotgun", "Phasewalk"),
    )
    world.set_rule(world.get_location("N-Sanity Island Star 7"), Has("Aku Aku"))
    world.set_rule(world.get_location("N-Sanity Island Star 8"), Has("Aku Aku"))

    # The Walking Dead: Saints, Sinners, & Mario
    world.set_rule(world.get_location(
        "The Walking Dead: Saints, Sinners, & Mario Star 1"),
        Has("Pizza Knight"),
    )
    world.set_rule(world.get_location(
        "The Walking Dead: Saints, Sinners, & Mario Star 2"),
        Has("Esteemed Mortal"),
    )
    world.set_rule(world.get_location(
        "The Walking Dead: Saints, Sinners, & Mario Star 3"),
        Has("Gadget Watch"),
    )
    world.set_rule(world.get_location(
        "The Walking Dead: Saints, Sinners, & Mario Star 4"),
        Has("Gadget Watch"),
    )
    world.set_rule(world.get_location(
        "The Walking Dead: Saints, Sinners, & Mario Star 5"),
        Has("Helmet & Drill"),
    )
    world.set_rule(world.get_location(
        "The Walking Dead: Saints, Sinners, & Mario Star 7"),
        HasAll("Inkling", "Doom Shotgun"),
    )
    world.set_rule(world.get_location(
        "The Walking Dead: Saints, Sinners, & Mario Star 8"),
        HasAll("Inkling", "Shock Rocket"),
    )

    # Mario in Hamsterball
    world.set_rule(world.get_location("Mario in Hamsterball Star 8"), Has("Hamster Ball"))

    # Environmental Station M
    world.set_rule(world.get_location("Environmental Station M Star 2"), Has("Dash Booster"))
    world.set_rule(world.get_location("Environmental Station M Star 3"), Has("Pizza Knight"))
    world.set_rule(world.get_location("Environmental Station M Star 6"), Has("Dash Booster"))
    world.set_rule(world.get_location(
        "Environmental Station M Star 7"),
        HasAll("Aku Aku", "Dash Booster"),
    )
    world.set_rule(world.get_location(
        "Environmental Station M Star 8"),
        HasAll("Helmet & Drill", "Shock Rocket"),
    )