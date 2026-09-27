from __future__ import annotations
from BaseClasses import Item, ItemClassification

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .World import MitmWorld

from .Global import LevelList

ITEM_NAME_TO_ID = {
    "Cutter" : 1,
    "Bubble Hat" : 2,
    "Inkling" : 3,
    "Shock Rocket" : 4,
    "Phasewalk" : 5,
    "Helmet & Drill" : 6,
    "Pizza Knight" : 7,
    "Chronos" : 8,
    "Doom Shotgun" : 9,
    "Gadget Watch" : 10,
    "HM Fly" : 11,
    "Aku Aku" : 12,
    "Esteemed Mortal" : 13,
    "Hamster Ball" : 14,
    "Dash Booster" : 15,

    "Compass" : 16,
    "Lon Lon Milk" : 17,
    "Magic Mirror" : 18,

    "Atreus' Artifact" : 19,

    "Power Star" : 20,
    "50 Coins" : 21,

    #22-36 Are Level Items

    "Blue Skull Key" : 37,
    "Red Skull Key" : 38,
    "Boat Key" : 39,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Cutter" : ItemClassification.progression,
    "Bubble Hat" : ItemClassification.progression,
    "Inkling" : ItemClassification.progression,
    "Shock Rocket" : ItemClassification.progression,
    "Phasewalk" : ItemClassification.progression,
    "Helmet & Drill" : ItemClassification.progression,
    "Pizza Knight" : ItemClassification.progression,
    "Chronos" : ItemClassification.progression,
    "Doom Shotgun" : ItemClassification.progression,
    "Gadget Watch" : ItemClassification.progression,
    "HM Fly" : ItemClassification.progression,
    "Aku Aku" : ItemClassification.progression,
    "Esteemed Mortal" : ItemClassification.progression,
    "Hamster Ball" : ItemClassification.progression,
    "Dash Booster" : ItemClassification.progression,

    "Compass" : ItemClassification.useful,
    "Lon Lon Milk" : ItemClassification.useful,
    "Magic Mirror" : ItemClassification.useful,

    "Atreus' Artifact" : ItemClassification.progression,

    "Power Star" : ItemClassification.progression,
    "50 Coins" : ItemClassification.filler,

    "Blue Skull Key" : ItemClassification.progression,
    "Red Skull Key" : ItemClassification.progression,
    "Boat Key" : ItemClassification.progression,
}

liid = 22
for level in LevelList:
    ITEM_NAME_TO_ID[level] = liid
    DEFAULT_ITEM_CLASSIFICATIONS[level] = ItemClassification.progression
    liid += 1

class MitmItem(Item):
    game = "Mario in the Multiverse"

def get_random_filler_item_name(world: MitmWorld) -> str:
    return "50 Coins"

def create_item_with_correct_classification(world: MitmWorld, name: str) -> MitmItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return MitmItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


valid_first_world_indices = [
    0, # ssu
    1, # mibb
    2, # oo
    4, # o
    5, # br
    6, # btcp
]

def create_all_items(world: MitmWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Cutter"),
        world.create_item("Bubble Hat"),
        world.create_item("Inkling"),
        world.create_item("Shock Rocket"),
        world.create_item("Phasewalk"),
        world.create_item("Helmet & Drill"),
        world.create_item("Pizza Knight"),
        world.create_item("Chronos"),
        world.create_item("Doom Shotgun"),
        world.create_item("Gadget Watch"),
        world.create_item("HM Fly"),
        world.create_item("Aku Aku"),
        world.create_item("Esteemed Mortal"),
        world.create_item("Hamster Ball"),
        world.create_item("Dash Booster"),

        world.create_item("Blue Skull Key"),
        world.create_item("Red Skull Key"),
        world.create_item("Boat Key"),
    ]

    #TODO: Make level items optional

    unlock_first = valid_first_world_indices[world.random.randint(0,5)]
    
    for i in range(15):
        if i == unlock_first:
            world.push_precollected(world.create_item(LevelList[i]))
        else:
            itempool.append(world.create_item(LevelList[i]))

    for i in range(120):
        itempool.append(world.create_item("Power Star") )

    # Items added due to special options
    if world.options.shopsanity:
        itempool.append(world.create_item("Power Star"))
        itempool.append(world.create_item("Compass"))
        itempool.append(world.create_item("Lon Lon Milk"))
        itempool.append(world.create_item("Magic Mirror"))
        itempool.append(world.create_item("Atreus' Artifact"))


    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool