#!/bin/bash
#
# Part of MariaDB Manager package
#
# This file is distributed as part of the MariaDB Manager package.
# It is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2013-2014 (c) SkySQL Corporation Ab
#
# Author      : Massimo Siani
# Version     : 1.1
# Date        : December 2013
# Description    : Generates a new API ID/key pair
#
# parameters    : $1 API ID


[[ $# -lt 1 ]] && exit 1

componentID=$1
componentFile=/etc/mariadbmanager/manager.ini
newKey=$(echo $RANDOM$(date)$RANDOM | md5sum | cut -f1 -d" ")
keyString="${componentID} = \"${newKey}\""
grep "^${componentID} = \"" ${componentFile} &>/dev/null
if [ "$?" != "0" ] ; then
    sed -i "/\[apikeys\]/a $keyString" $componentFile
fi
