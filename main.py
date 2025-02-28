import time
from vlc_rpc.rpc_manager import RPCManager
from vlc_rpc.process_monitor import ProcessMonitor
from vlc_rpc.utils import load_config

def main():
    client_id = load_config()
    rpc_manager = RPCManager(client_id)
    process_monitor = ProcessMonitor()

    print("VLC Rich Presence is running. Press Ctrl+C to stop.")
    last_media = None

    try:
        while True:
            vlc_proc = process_monitor.find_vlc_process()
            if vlc_proc:
                media_name = process_monitor.get_media_info(vlc_proc)
                if media_name != last_media:
                    rpc_manager.update_rpc(media_name)
                    last_media = media_name
            elif last_media:
                rpc_manager.clear_rpc()
                last_media = None
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        rpc_manager.clear_rpc()

if __name__ == "__main__":
    main()