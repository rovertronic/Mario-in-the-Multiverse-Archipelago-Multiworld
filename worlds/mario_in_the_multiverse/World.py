from BaseClasses import Item, ItemClassification, MultiWorld, Tutorial, LocationProgressType, Region, Entrance
from worlds.AutoWorld import WebWorld, World

from . import Options as mitm_options
from . import Items
from . import Locations
from . import Rules

from .Global import LevelList

class MitmWebWorld(WebWorld):
    game = "Mario in the Multiverse"
    theme = "partyTime"

class MitmWorld(World):
    game = "Mario in the Multiverse"
    web = MitmWebWorld()

    item_name_to_id = Items.ITEM_NAME_TO_ID
    location_name_to_id = Locations.LOCATION_NAME_TO_ID

    options_dataclass = mitm_options.MitmOptions
    options: mitm_options.MitmOptions

    origin_region_name = "Hub"

    def pre_fill(self):
        if not self.options.shopsanity:
            self.get_location("Shop Item 1").place_locked_item( self.create_item("Compass"))
            self.get_location("Shop Item 2").place_locked_item( self.create_item("Magic Mirror"))
            self.get_location("Shop Item 3").place_locked_item( self.create_item("Lon Lon Milk"))
            self.get_location("Shop Item 4").place_locked_item( self.create_item("Power Star"))
            self.get_location("Shop Item 5").place_locked_item( self.create_item("Atreus' Artifact"))

    def create_regions(self):
        self.main_region = Region("Hub",self.player,self.multiworld)
        self.multiworld.regions += [self.main_region]

        for level in LevelList:
            # The entrance "level" to region "level" requires item "level"
            region = Region( level, self.player, self.multiworld )
            self.multiworld.regions += [ region ]

            self.main_region.connect( self.get_region(level) , level + " Entrance")


        Locations.create_all_locations(self)

    def create_item(self, name: str) -> Items.MitmItem:
        return Items.create_item_with_correct_classification(self, name)

    def create_items(self):
        Items.create_all_items(self)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)

    def set_rules(self) -> None:
        Rules.set_all_rules(self)