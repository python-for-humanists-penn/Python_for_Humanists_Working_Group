#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:24:59 2019

@author: jdummer
"""

import yaml
import os
import glob


def extract_yml(filename):

    yml_lines = []
    with open(filename, encoding='utf8') as file:
        for line in file:
            if line.strip() == "---":
                break
        for line in file:
            if line.strip() == "---":
                break
            else:
                yml_lines.append(line)

    yml_string = "".join(yml_lines)
    return yaml.load(yml_string)


if __name__ == "__main__":

    post_dir = '.'
    tag_dir = 'tag/'

    filenames = glob.glob(os.path.join(post_dir, '*md'))
    total_tags = []
    for filename in filenames:
        post_yaml = extract_yml(filename)
        if post_yaml is not None:
            tags = post_yaml.get('tags', [])
            total_tags.extend(tags)
    total_tags = set(total_tags)
    print(total_tags)
    print(filenames)

    old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())


#  print(extract_yml('./2019-02-15-the-bridges-of-madison-county.md'))
