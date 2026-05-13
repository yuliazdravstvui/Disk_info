import shutil
import os

def get_size(bytes_val):
    for unit in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.1f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.1f} ПБ"

def get_disk_info():
    if os.name == 'nt':  # Windows
        drives = []
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            path = letter + ':/'
            if os.path.exists(path):
                drives.append(path)
    else:  # Linux/Mac
        drives = ['/']
        if os.path.exists('/mnt'):
            for item in os.listdir('/mnt'):
                path = os.path.join('/mnt', item)
                if os.path.ismount(path):
                    drives.append(path)

    disks = []
    for path in drives:
        try:
            usage = shutil.disk_usage(path)
            total = usage.total
            used = usage.used
            free = usage.free
            percent = (used / total) * 100

            disks.append({
                'name': path,
                'total': get_size(total),
                'used': get_size(used),
                'free': get_size(free),
                'percent': round(percent, 1),
                'bar_width': percent
            })
        except (PermissionError, OSError):
            disks.append({
                'name': path,
                'total': 'Нет доступа',
                'used': '-',
                'free': '-',
                'percent': 0,
                'bar_width': 0
            })

    return disks