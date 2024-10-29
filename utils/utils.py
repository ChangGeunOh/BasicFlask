from typing import Optional
from pathlib import Path
from flask import Flask, jsonify
import time


def get_media_type(file: Path):
        
    file_extension = file.suffix.lower()
    if file_extension == ".pdf":
        media_type = "application/pdf"
    elif file_extension in [".xls", ".xlsx"]:
        media_type = "application/vnd.ms-excel"  # .xls
        if file_extension == ".xlsx":
            media_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    elif file_extension == ".doc":
        media_type = "application/msword"
    elif file_extension == ".docx":
        media_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    elif file_extension == ".jpg" or file_extension == ".jpeg":
        media_type = "image/jpeg"
    elif file_extension == ".png":
        media_type = "image/png"
    else:
        media_type = "application/octet-stream"  # 기본값 (이진 파일)

    return media_type




def getCurrentTimeMils():
    return round(time.time() * 1000)