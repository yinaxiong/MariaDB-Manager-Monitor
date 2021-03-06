%define _topdir	 	%(echo $PWD)/
%define name		MariaDB-Manager-Monitor
%define release		##RELEASE_TAG##
%define version 	##VERSION_TAG##
%define buildroot 	%{_topdir}/%{name}-%{version}-%{release}-root
%define install_path	/usr/local/skysql/monitor/

BuildRoot:		%{buildroot}
BuildArch:              noarch
Summary: 		MariaDB Manager Monitor
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-%{release}.tar.gz
Prefix: 		/
Group: 			Development/Tools
Requires:		libMariaDB-Manager-java >= 0.1-12
#BuildRequires:		java-1.7.0-openjdk

%description
MariaDB Manager is a tool to manage and monitor a set of MariaDB
servers using the Galera multi-master replication form Codership.
This component is the monitor for the MariaDB Manager, it probes
the databases within control of the system gathering performance
and statistics data from the servers.

%prep

%setup -q

%build

%post
chkconfig --add mariadb-manager-monitor
# : > /etc/mariadbmanager/manager.ini
#if ! grep -q '\[monitor\]' /etc/mariadbmanager/manager.ini ; then
#    cat %{install_path}manager_monitor.ini >> /etc/mariadbmanager/manager.ini
#fi

#%{install_path}generateAPIkey.sh 3
rm -f %{install_path}generateAPIkey.sh
rm -f %{install_path}manager_monitor.ini

%install
mkdir -p $RPM_BUILD_ROOT%{install_path}
cp ClusterMonitor.jar $RPM_BUILD_ROOT%{install_path}
cp generateAPIkey.sh $RPM_BUILD_ROOT%{install_path}
cp manager_monitor.ini $RPM_BUILD_ROOT%{install_path}
mkdir -p $RPM_BUILD_ROOT/etc/init.d/
cp mariadb-manager-monitor $RPM_BUILD_ROOT/etc/init.d/
mkdir -p $RPM_BUILD_ROOT/etc/mariadbmanager/

%clean

%files
%defattr(-,root,root)
%{install_path}
%{install_path}ClusterMonitor.jar
%{install_path}generateAPIkey.sh
%{install_path}manager_monitor.ini
/etc/init.d/mariadb-manager-monitor

%changelog
