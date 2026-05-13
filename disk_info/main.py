import shutil
import os


def get_size(bytes_val):
    for unit in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.1f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.1f} ПБ"


def progress_bar(percent, length=30):
    filled = int(length * percent / 100)
    bar = '█' * filled + '░' * (length - filled)
    return f"[{bar}] {percent:.1f}%"


def main():
    print("\n=== АНАЛИЗ ДИСКОВ ===\n")

    if os.name == 'nt':
        drives = []
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            path = letter + ':/'
            if os.path.exists(path):
                drives.append(path)
    else:
        drives = ['/']

    for path in drives:
        try:
            usage = shutil.disk_usage(path)
            total = usage.total
            used = usage.used
            free = usage.free
            percent = (used / total) * 100

            print(f"Диск: {path}")
            print(f"  Всего:    {get_size(total)}")
            print(f"  Занято:   {get_size(used)}")
            print(f"  Свободно: {get_size(free)}")
            print(f"  {progress_bar(percent)}\n")
        except (PermissionError, OSError):
            print(f"Диск {path}: нет доступа\n")


if __name__ == "__main__":
    main()
