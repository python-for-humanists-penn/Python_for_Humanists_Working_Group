#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:24:59 2019

@author: jdummer
"""

import yaml
import os
import glob

def extract_yaml(filename):
    yml_lines = []
    with open(filename, encoding='utf8') as file:
        for line in file:
            if line.strip() == '---':
                break
        for line in file:
            if line.strip() == '---':
                break
            else:
                yml_lines.append(line)

    yml_string = "".join(yml_lines)
    return yaml.load(yml_string)

if __name__ == '__main__':
    post_dir = '_posts'
    tag_dir = 'tag/'

    filenames = glob.glob(os.path.join(post_dir, '*md'))
    total_tags = []
    for filename in filenames:
        post_yaml = extract_yaml(filename)
        if post_yaml is not None:
            tags = post_yaml.get('tags', [])
            total_tags.extend(tags)
    total_tags = set(total_tags)
    print(total_tags)

    for tag in total_tags:
        tag_filename = tag_dir + tag.replace(' ', '+') + '.md'
        if os.path.exists(tag_dir + filename):
            pass
        else:
            tag_page = open(tag_filename, 'w')
            write_str = '---\nexclude: true\nlayout: tagpage\ntitle: \"Tagged: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
            tag_page.write(write_str)
            tag_page.close()
    print("Tags generated, count", total_tags.__len__())