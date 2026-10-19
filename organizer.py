from pathlib import Path
import shutil

FOLDERS = {
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Videos": {".mp4", ".mov", ".avi", ".mkv"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp"},
}


def category_for(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FOLDERS.items():
        if extension in extensions:
            return category

    return "Other"


def unique_destination(destination):
    """File peru already unte, vere peru create chestundi."""
    if not destination.exists():
        return destination

    number = 1
    while True:
        new_name = f"{destination.stem}_{number}{destination.suffix}"
        candidate = destination.with_name(new_name)

        if not candidate.exists():
            return candidate

        number += 1


def main():
    folder_text = input("Organize cheyyalsina folder path enter cheyyi: ").strip()
    source_folder = Path(folder_text.strip('"')).expanduser()

    if not source_folder.is_dir():
        print("Aa folder dorakaledu. Path correct-ga undho check cheyyi.")
        return

    files = [item for item in source_folder.iterdir() if item.is_file()]

    if not files:
        print("Ee folder-lo organize cheyyadaniki files levu.")
        return

    print(f"\n{source_folder} lo {len(files)} file(s) unnayi.")
    confirm = input("Ee files-ni category folders-loki move cheyyala? (yes/no): ").lower()

    if confirm != "yes":
        print("Cancel chesanu; files move cheyyaledu.")
        return

    moved = 0
    errors = 0

    for file_path in files:
        category = category_for(file_path)
        category_folder = source_folder / category
        destination = unique_destination(category_folder / file_path.name)

        try:
            category_folder.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {category}/")
            moved += 1
        except (PermissionError, OSError) as error:
            print(f"Move cheyyalekapoyanu: {file_path.name} ({error})")
            errors += 1

    print("\n--- Summary ---")
    print(f"Moved files: {moved}")
    print(f"Errors: {errors}")


if __name__ == "__main__":
    main()