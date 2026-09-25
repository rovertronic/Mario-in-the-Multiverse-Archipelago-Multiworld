import asyncio

from PyMemoryEditor import OpenProcess
from PyMemoryEditor import ProcessOperationsEnum

import CommonClient
from CommonClient import CommonContext, server_loop, get_base_parser, handle_url_arg
from argparse import Namespace

import colorama

import logging


archipelago_buffer_start = 0x0
process = None

def n64_string(s):
    data = s.encode("ascii")

    # Pad with spaces to a multiple of 4 bytes
    data += b" " * (-len(data) % 4)

    # Reverse each 4-byte word
    return b"".join(
        data[i:i+4][::-1]
        for i in range(0, len(data), 4)
    )

def name_to_model_id(name) -> int:
    name_lower = name.lower()

    # Power Stars (Any game)
    if "star" in name_lower:
        return 2
    
    # Abilities
    if name_lower == "cutter":
        return 6

    if name_lower == "bubble hat":
        return 7

    if name_lower == "inkling":
        return 8

    if "rocket" in name_lower:
        return 9

    if name_lower == "phasewalk":
        return 10

    if "helmet" in name_lower:
        return 11

    if name_lower == "pizza knight" or ("armor" in name_lower):
        return 12

    if name_lower == "chronos" or "sword" in name_lower:
        return 13

    if "gun" in name_lower:
        return 14

    if name_lower == "gadget watch":
        return 15

    if name_lower == "hamsterball":
        return 19

    if name_lower == "hm fly" or "ball" in name_lower:
        return 16

    if name_lower == "aku aku" or "mask" in name_lower:
        return 17

    if name_lower == "esteemed mortal":
        return 18

    if name_lower == "dash booster":
        return 19

    # Generic models (For fun)
    if "bomb" in name_lower or "explosive" in name_lower:
        return 3

    if "stone" in name_lower or "rock" in name_lower:
        return 4

    if "hp" in name_lower or "heart" in name_lower or "health" in name_lower:
        return 5

    return 1


class MitmContext(CommonContext):
    game = "Mario in the Multiverse"
    items_handling = 7

    async def server_auth(self, password_requested=False):
        global process
        global archipelago_buffer_start

        logging.getLogger("Client").info("Waiting for Mario in the Multiverse in Retroarch.exe")
        while process == None:
            try:
                process = OpenProcess(name = "retroarch.exe")

                matches = list(process.search_by_value(str, value = n64_string("MITM AP BUFFER  ")))
                for address in matches:
                    print(f"Found at 0x{address:X}")
                    archipelago_buffer_start = address
                    # 

                process.write_process_memory(archipelago_buffer_start + 4*4, int, value = 1)

                logging.getLogger("Client").info("Connected to Mario in the Multiverse in Retroarch.exe")
            except:
                pass

            await asyncio.sleep(0.1)

        await self.get_username()
        await self.send_connect(game=self.game)

    def on_package(self, cmd, args):
        print(cmd)
        print(args)
            
        if cmd == "Connected":
            process.write_process_memory(archipelago_buffer_start + 4*5, int, value = 1)
        
        if cmd == "ReceivedItems":
            for item in args["items"]:
                sendstr = "Got " + self.item_names.lookup_in_game(item.item) + " from " + self.player_names[item.player]

                if item.player == self.slot:
                    sendstr = "Found your " + self.item_names.lookup_in_game(item.item)

                process.write_process_memory(archipelago_buffer_start + 4*8, str, value = n64_string(sendstr + '\0') )
                process.write_process_memory(archipelago_buffer_start + 4*22, int, value = 400)

                mem_slot = (item.item-1) // 32
                mem_bit = (item.item-1) % 32
                mem_slot *= 4

                curflags = process.read_process_memory(archipelago_buffer_start + 4*20 + mem_slot, int)
                process.write_process_memory(archipelago_buffer_start + 4*20 + mem_slot, int, value = curflags | (1 << mem_bit))


async def main():
    parser = CommonClient.get_base_parser()
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    args = parser.parse_args()

    ctx = MitmContext(args.connect, args.password)

    ctx.auth = args.name

    ctx.run_gui()
    ctx.run_cli()

    ctx.ui.base_title = "Mario in the Multiverse Client"

    while not ctx.exit_event.is_set():
        if ctx.slot is not None:

            # Scout to recieve item and player names
            if len(ctx.locations_info) == 0:
                await ctx.send_msgs([{
                    "cmd": "LocationScouts",
                    "locations":  list(range(1,6)),
                    "create_as_hint" : True
                }])

                #stars
                await ctx.send_msgs([{
                    "cmd": "LocationScouts",
                    "locations":  list(range(9, 120 + 9))
                }])

                await ctx.send_msgs([{
                    "cmd": "LocationScouts",
                    "locations":  list(range(140, 140 + 15))
                }])

            # Send locations
            location_get = process.read_process_memory(archipelago_buffer_start + 4*6, int)
            if location_get > 0:
                await ctx.check_locations({location_get})

                info = ctx.locations_info.get(location_get)
                if info:
                    sendstr = "Sent " + ctx.item_names.lookup_in_slot( info.item, info.player ) + " to " + ctx.player_names[info.player]
                    process.write_process_memory(archipelago_buffer_start + 4*8, str, value = n64_string(sendstr + '\0') )
                    process.write_process_memory(archipelago_buffer_start + 4*22, int, value = 400)

                process.write_process_memory(archipelago_buffer_start + 4*6, int, value = 0)

            # Send Star Count
            star_count = 0
            for item in ctx.items_received:
                if item.item == 20:
                    star_count += 1

            process.write_process_memory(archipelago_buffer_start + 4*7, int, value = star_count)

            # Send model ids upon request
            ap_model_request = process.read_process_memory(archipelago_buffer_start + 4*31, int)
            if ap_model_request > 0:
                print("ok...")
                info = ctx.locations_info.get(ap_model_request)
                if info:
                    print("GET SENT!")
                    process.write_process_memory(archipelago_buffer_start + 4*32, int, value = name_to_model_id(ctx.item_names.lookup_in_slot(info.item,info.player) )  )

        await asyncio.sleep(0.1)

asyncio.run(main())

