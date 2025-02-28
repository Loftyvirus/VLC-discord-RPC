from pypresence import Presence
import sys

class RPCManager:
    def __init__(self, client_id):
        self.client_id = client_id
        self.rpc = self.initialize_rpc()

    def initialize_rpc(self):
        try:
            rpc = Presence(self.client_id)
            rpc.connect()
            return rpc
        except Exception as e:
            print(f"Failed to connect to Discord: {e}")
            sys.exit(1)

    def update_rpc(self, media_name):
        if media_name:
            print(f"Currently watching: {media_name}")
            self.rpc.update(
                details=f"Watching {media_name}",
                state="on VLC Media Player",
                large_image="vlc_logo",
                large_text="VLC Media Player",
                small_image="small_icon",
                small_text="Watching"
            )
        else:
            self.rpc.clear()

    def clear_rpc(self):
        self.rpc.clear()