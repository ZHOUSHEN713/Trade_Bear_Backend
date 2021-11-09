import os
import hashlib
from datetime import datetime
from flask import current_app


class FileOperator:
    def __init__(self):
        self.root_dir_path = "/home/ubuntu/Trade_Bear_Backend/static/"
        self.hl = hashlib.md5()

    def save_img(self, file):
        t = file.filename + str(datetime.now())
        self.hl.update(t.encode(encoding='utf-8'))
        md5_str = self.hl.hexdigest()
        ext = file.filename.split('.')[-1]
        store_path = os.path.join(self.root_dir_path, f"figures/{md5_str}.{ext}")
        file.save(store_path)
        address = f"http://81.70.0.250:8080/static/figures/{md5_str}.{ext}"
        return address


file_operator = FileOperator()
