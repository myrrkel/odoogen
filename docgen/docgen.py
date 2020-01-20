#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fnmatch
import logging
import os
import sys

import html2markdown


logger = logging.getLogger(__name__)

class DocGen:

    addons_dir = ""

    def __init__(self, addons_dir=""):
        if addons_dir:
            self.addons_dir = addons_dir


    def set_addons_dir(self, addons_dir):
        self.addons_dir = addons_dir

    def get_all_markdown_docs(self, module_dir=""):
        res = ""
        dir_path = module_dir or self.addons_dir
        dir_list = next(os.walk(dir_path))[1]
        dir_list.sort()
        for i, dir_name in enumerate(dir_list):
            logger.info("md_dir_name: %s", dir_name)
            if res: res += "\n\r-----\n"

            res += "### "+os.path.basename(dir_name)+"\n"
            res += get_markdown_doc(os.path.join(dir_path, str(dir_name)))

            # iProgress = round((i/len(dir_list))*100)
            # progress_changed.emit(iProgress)
        logger.info("Markdown: %s", res)
        return res

def get_markdown_doc(module_dir):
    doc_text = ""

    try:
        files = os.listdir(module_dir)
    except FileNotFoundError:
        files = []

    files = [os.path.join(module_dir, str(file)) for file in files if fnmatch.fnmatch(file.lower(), '*.md')]
    files.sort()

    for file in files:
        try:
            with open(file, 'rU') as f:
                text = f.read()
                text = text.replace('](./', '](%s/' % module_dir)

        except Exception as e:
            logger.error(e)
        else:
            doc_text += text

    return doc_text
