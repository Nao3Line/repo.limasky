#!/usr/bin/env python3
import os, hashlib

addons_xml = u'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'

for addon in os.listdir("."):
    if os.path.isdir(addon) and addon != ".git":
        addon_xml = os.path.join(addon, "addon.xml")
        if os.path.exists(addon_xml):
            with open(addon_xml, "r", encoding="utf-8") as f:
                addons_xml += f.read().strip() + "\n"

addons_xml += u"</addons>\n"

with open("addons.xml", "w", encoding="utf-8") as f:
    f.write(addons_xml)

md5 = hashlib.md5(addons_xml.encode("utf-8")).hexdigest()
with open("addons.xml.md5", "w") as f:
    f.write(md5)
