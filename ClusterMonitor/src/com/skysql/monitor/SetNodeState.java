/*
 * This file is distributed as part of the MariaDB Manager.  It is free
 * software: you can redistribute it and/or modify it under the terms of the
 * GNU General Public License as published by the Free Software Foundation,
 * version 2.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program; if not, write to the Free Software Foundation, Inc., 51
 * Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Copyright 2012-2014 SkySQL Corporation Ab
 */

package com.skysql.monitor;

import java.util.*;

import com.skysql.java.Logging;
import com.skysql.java.MonData;

/**
 * Standalone program for setting the Node state. No longer used.
 * 
 * @author Mark Riddoch
 *
 */
public class SetNodeState {
	
	MonData		m_confdb;
	int			m_systemID;
	int			m_nodeid;
	
	public static void main( String[] args )
	{
		if (args.length != 4)
		{
			Logging.error("Usage: SetNodeState <System ID> <Node ID> <dbfile> <state>");
			System.exit(1);
		}
		SetNodeState obj = new SetNodeState(new Integer(args[0]).intValue(), new Integer(args[1]).intValue(), args[2]);
		obj.setState(args[3]);
	}
	
	public SetNodeState(int systemID, int nodeID, String dbfile)
	{
		m_confdb = new MonData(systemID);
		m_nodeid = nodeID;
		m_systemID = systemID;
	}
	
	public void setState(String state)
	{
		int monid = m_confdb.getNamedMonitor("Node State");
		if (monid == -1)
		{
			Logging.error("Can't find Monitor \"Node State\".");
			System.exit(1);
		}
		int stateid = m_confdb.getNodeStateId(state);
		if (stateid == -1)
		{
			Logging.error("Unknown Node state " + state);
			Logging.error("Valid states are:");
			List<String> states = m_confdb.getNodeValidStates();
			Iterator<String> it = states.iterator();
			while (it.hasNext())
			{
				Logging.error("    " + it.next());
			}
			System.exit(1);
		}
		String newValue = (new Integer(stateid)).toString();
		m_confdb.monitorData(m_nodeid, monid, newValue);
		m_confdb.setNodeState(m_nodeid, stateid);
	}
}
