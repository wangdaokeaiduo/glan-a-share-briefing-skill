import os
import sys
import glob
import shutil
import time

def backup_file(target_file):
    if not os.path.exists(target_file):
        print(f"Error: {target_file} does not exist.")
        return

    # Define backups directory relative to the skill directory
    skill_dir = "/Users/wangdao/Documents/重要文档/www/touzibiao/.agents/skills/glan-sleep-optimizer"
    backup_dir = os.path.join(skill_dir, "backups")
    os.makedirs(backup_dir, exist_ok=True)

    base_name = os.path.basename(target_file)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_name = f"{base_name}.{timestamp}.bak"
    backup_path = os.path.join(backup_dir, backup_name)

    # Copy file
    shutil.copy2(target_file, backup_path)
    print(f"Backup created: {backup_path}")

    # Prune old backups (keep last 3)
    search_pattern = os.path.join(backup_dir, f"{base_name}.*.bak")
    existing_backups = sorted(glob.glob(search_pattern))
    
    if len(existing_backups) > 3:
        for old_backup in existing_backups[:-3]:
            os.remove(old_backup)
            print(f"Removed old backup: {old_backup}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python backup_framework.py <path_to_file>")
        sys.exit(1)
    backup_file(sys.argv[1])
