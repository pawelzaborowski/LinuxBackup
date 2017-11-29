#!/usr/bin/env python
#
import os

os.system("find /home/quanzig/ASK-projekt/Backups* -mtime +30 -exec rm {} \;")

