from __future__ import annotations
from BaseClasses import ItemClassification, Location
from . import Items

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .World import MitmWorld

from .Global import LevelList
from .Global import AbilityList

LOCATION_NAME_TO_ID = {
    "Shop Item 1" : 1,
    "Shop Item 2" : 2,
    "Shop Item 3" : 3,
    "Shop Item 4" : 4,
    "Shop Item 5" : 5,

    #"Bob-Omb Battlefield Painting" : 9

    "Cutter" : 140,
    "Bubble Hat" : 141,
    "Inkling" : 142,
    "Shock Rocket" : 143,
    "Phasewalk" : 144,
    "Helmet & Drill" : 145,
    "Pizza Knight" : 146,
    "Chronos" : 147,
    "Doom Shotgun" : 148,
    "Gadget Watch" : 149,
    "HM Fly" : 150,
    "Aku Aku" : 151,
    "Esteemed Mortal" : 152,
    "Hamster Ball" : 153,
    "Dash Booster" : 154,
}

idinc = 9
for level in LevelList:
    for i in range(8):
        location_name = level + " Star " + str(i+1)
        LOCATION_NAME_TO_ID[location_name] = idinc
        idinc += 1

idinc = 140
for ability in AbilityList:
    location_name = ability
    LOCATION_NAME_TO_ID[location_name] = idinc
    idinc += 1



class MitmLocation(Location):
    game = "Mario in the Multiverse"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: MitmWorld) -> None:
    create_regular_locations(world)

def create_regular_locations(world: MitmWorld) -> None:

    # Shop Locations
    for i in range(5):
        shop_item = MitmLocation(
            world.player, "Shop Item " + str(i+1) , world.location_name_to_id["Shop Item " + str(i+1)], world.get_region("Hub")
        )
        world.main_region.locations.append(shop_item)

    # Ability Locations
    for i in range(15):
        world.get_region( LevelList[i]  ).locations.append(MitmLocation(world.player, AbilityList[i], world.location_name_to_id[ AbilityList[i] ], world.get_region( LevelList[i] )) )

    # Star Locations
    for level in LevelList:
        for i in range(8):
            location_name = level + " Star " + str(i+1)
            world.get_region(level).locations.append(MitmLocation(world.player, location_name, world.location_name_to_id[location_name], world.get_region(level)) )

    