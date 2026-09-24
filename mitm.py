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
                print(item.item)
                sendstr = "Got " + self.item_names.lookup_in_game(item.item) + " from " + self.player_names[item.player]
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

            location_get = process.read_process_memory(archipelago_buffer_start + 4*6, int)
            if location_get > 0:
                print("sent: " + str(location_get))
                await ctx.check_locations({location_get})
                process.write_process_memory(archipelago_buffer_start + 4*6, int, value = 0)

            star_count = 0
            for item in ctx.items_received:
                if item.item == 20:
                    star_count += 1

            process.write_process_memory(archipelago_buffer_start + 4*7, int, value = star_count)

        await asyncio.sleep(0.1)

asyncio.run(main())

