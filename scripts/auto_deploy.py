import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from pathlib import Path

class SiteHandler(FileSystemEventHandler):
    def __init__(self, site_root):
        self.site_root = site_root
        self.public_dir = os.path.join(site_root, 'public')
        self.last_build_time = 0
        self.cooldown = 5  # Cooldown period in seconds

    def rebuild_and_deploy(self):
        current_time = time.time()
        if current_time - self.last_build_time < self.cooldown:
            return
        
        self.last_build_time = current_time
        print("\n🔄 Changes detected! Rebuilding site...")
        
        try:
            # Run the category update script
            print("📑 Updating categories...")
            subprocess.run(['python3', os.path.join(self.site_root, 'scripts', 'update_categories.py')], 
                         cwd=self.site_root, check=True)

            # Build the site
            print("🏗️ Building site with Hugo...")
            subprocess.run(['hugo', '--minify'], cwd=self.site_root, check=True)

            # Deploy to GitHub
            print("🚀 Deploying to GitHub...")
            subprocess.run(['git', 'add', '.'], cwd=self.public_dir, check=True)
            subprocess.run(['git', 'commit', '-m', 'auto: rebuild and deploy site'], 
                         cwd=self.public_dir, check=True)
            subprocess.run(['git', 'push', '-f', 'origin', 'main'], 
                         cwd=self.public_dir, check=True)
            
            print("✅ Site successfully rebuilt and deployed!")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error during deployment: {str(e)}")

    def on_modified(self, event):
        if event.is_directory:
            return
        
        # Ignore changes in public directory and .git directories
        if '/public/' in event.src_path or '/.git/' in event.src_path:
            return
            
        # Only rebuild for relevant file changes
        if any(event.src_path.endswith(ext) for ext in ['.md', '.html', '.toml', '.css', '.js']):
            self.rebuild_and_deploy()

def watch_site(site_root):
    event_handler = SiteHandler(site_root)
    observer = Observer()
    observer.schedule(event_handler, site_root, recursive=True)
    observer.start()
    
    print(f"👀 Watching for changes in {site_root}")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Stopping file watcher")
    
    observer.join()

if __name__ == "__main__":
    site_root = "/Users/air-sr/Library/CloudStorage/GoogleDrive-sunil@axysanalytics.com/My Drive/Learn AI TV"
    watch_site(site_root)
