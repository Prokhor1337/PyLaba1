import json
import os
from threading import Lock

class Assistant:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.lock = Lock()
        self.notes = []
        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            self._save()
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.notes = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.notes = []
            self._save()

    def _save(self):
        with self.lock:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def add_note(self, note):
        self.notes.append(note)
        self._save()

    def list_notes(self):
        return self.notes

    def search_notes(self, keyword):
        return [n for n in self.notes if keyword.lower() in n.lower()]
