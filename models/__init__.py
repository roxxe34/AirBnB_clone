#!/usr/bin/python3
"""Main package of project"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
