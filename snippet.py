# -*- coding: utf-8 -*-

"""Snippet Engine.
Synopsis: <trigger> <filter>"""

from albert import *
import os
import time

__title__ = "Snippet Engine"
__version__ = "0.4.1"
__triggers__ = "s "
__authors__ = "Dmitry Kolosov"

SNIPPET_PATH = '/home/mitrich/projects/my/snippets'

def handleQuery(query):
    if not query.isTriggered:
        return

    # # avoid rate limiting
    time.sleep(0.1)
    if not query.isValid:
        return

    search = query.string.strip().lower()

    results = []
    
    for currentpath, folders, files in os.walk(SNIPPET_PATH):
        for file in files:
            fullpath = os.path.join(currentpath, file)
            with open(fullpath) as content:
                textContent = "/n".join(content.readlines())
                if search in file.lower() or search in textContent.lower():
                    results.append(
                        Item(id=__title__,
                            text=file,
                            subtext=textContent,
                            completion=file,
                            actions=[
                                ClipAction("Copy", textContent)
                            ]
                        )
                    )

    return results   
