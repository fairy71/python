import os
import json
import threading
import queue
from datetime import datetime

class FileIndexer:
    def __init__(self, root_dir, cache_file="file_index.json"):
        self.root_dir = root_dir
        self.cache_file = cache_file
        self.index = {}
        self.lock = threading.Lock()

    def build_index(self):
        print(f"[INFO] Building index for: {self.root_dir}")
        q = queue.Queue()
        q.put(self.root_dir)

        def worker():
            while not q.empty():
                try:
                    path = q.get_nowait()
                except queue.Empty:
                    break

                if os.path.isdir(path):
                    for f in os.listdir(path):
                        q.put(os.path.join(path, f))
                else:
                    self._add_file(path)
                q.task_done()

        threads = []
        for _ in range(8):  # 8 worker threads
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)

        q.join()
        for t in threads:
            t.join()

        self._save_cache()
        print(f"[INFO] Index built with {len(self.index)} files.")

    def _add_file(self, path):
        ext = os.path.splitext(path)[1].lower()
        with self.lock:
            self.index[path] = {
                "extension": ext,
                "size": os.path.getsize(path),
                "modified": datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
            }

    def _save_cache(self):
        with open(self.cache_file, "w") as f:
            json.dump(self.index, f, indent=2)

    def load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "r") as f:
                self.index = json.load(f)
            print(f"[INFO] Loaded {len(self.index)} files from cache.")
        else:
            print("[INFO] No cache found. Please build index first.")

    def search(self, keyword=None, extension=None):
        results = []
        for path, meta in self.index.items():
            if keyword and keyword.lower() not in os.path.basename(path).lower():
                continue
            if extension and meta["extension"] != extension.lower():
                continue
            results.append(path)
        return results


if __name__ == "__main__":
    root = input("Enter directory to index: ").strip()
    engine = FileIndexer(root)

    choice = input("Load cache (l) or Build new index (b)? ").lower()
    if choice == "l":
        engine.load_cache()
    else:
        engine.build_index()

    while True:
        query = input("\nSearch (keyword or 'exit'): ").strip()
        if query == "exit":
            break
        ext = input("Filter by extension (or leave blank): ").strip()
        results = engine.search(keyword=query if query else None,
                                extension=ext if ext else None)

        print(f"[RESULT] Found {len(results)} files:")
        for r in results[:20]:  # show only first 20
            print("   ", r)
