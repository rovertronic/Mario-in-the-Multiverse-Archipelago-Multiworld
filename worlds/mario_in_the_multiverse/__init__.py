from .World import MitmWorld as MitmWorld

from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .mitm_client import start_mitm_client
    launch(start_mitm_client, name="Mario in the Multiverse Client", args=args)

components.append(
    Component(
        "Mario in the Multiverse Client",
        func=run_client,
        game_name="Mario in the Multiverse",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)