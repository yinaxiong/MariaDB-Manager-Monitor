%define _topdir	 	%(echo $PWD)/
%define name			skysql_monitor
%define release		1
%define version 	0.1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define install_path	/usr/local/skysql/monitor/

BuildRoot:	%{buildroot}
Summary: 		SkySQL monitor
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/
Group: 			Development/Tools
Requires:		java-1.6.0-openjdk aws-apitools-ec2 skysql_aws_tools
BuildRequires:		java-1.6.0-openjdk skysql_aws_tools

%description
SkySQL monitor

%prep

%setup -q

%build

javac -d . -classpath `find /usr/local/skysql/skysql_aws/*.jar | tr '\n' ':' `  `find src/com/skysql/monitor | grep \.java`
jar cf ClusterMonitor.jar com/skysql/monitor/*.class

%install
mkdir -p $RPM_BUILD_ROOT%{install_path}
cp ClusterMonitor.jar  $RPM_BUILD_ROOT%{install_path}
cp monitor/ClusterMonitor.sh  $RPM_BUILD_ROOT%{install_path}

%clean

%files
%defattr(-,root,root)
%{install_path}
%{install_path}ClusterMonitor.jar
%{install_path}ClusterMonitor.sh

