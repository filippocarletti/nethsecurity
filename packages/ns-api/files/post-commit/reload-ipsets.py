#!/usr/bin/python

#
# Copyright (C) 2024 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-2.0-only
#

# This script forces ipset reload: they are not correctly reloaded by fw4 reload

import subprocess

force_reload = False

if 'firewall' in changes:
    for change in changes['firewall']:
        if 'ipset' in change:
            force_reload = True
            break

if 'objects' in changes:
    force_reload = True

if force_reload:
    subprocess.run(["/sbin/fw4", "restart"])
    # reload dns objects, due to restart they're emptied out
    subprocess.run(["/usr/bin/ns-objects-reload-dns"])
