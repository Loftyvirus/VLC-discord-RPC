import psutil
import os

class ProcessMonitor:
    @staticmethod
    def find_vlc_process():
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'vlc.exe':
                return proc
        return None

    @staticmethod
    def get_media_info(proc):
        try:
            for arg in proc.cmdline():
                if arg.endswith(('.mkv', '.mp4', '.avi', '.mov', '.mp3', '.flac', '.wav')):
                    return os.path.basename(arg)
            return None
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return None