#
# spec file for package ads
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:		ads
Version:	1.2
Release:	1
License:	GPL-3.0
Summary:	Swiss army knife for samba
Url:		http://www.github.com/dmulder/ads
Group:		Productivity/Networking/Samba
Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:   samba-client
Requires:   python-pam
Requires:   python-netifaces
Requires:   python-ldap
Requires:   krb5-client
Requires:   samba-python
Requires:   python2-dnspython
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python

%description
Active Directory services tool for samba.
For join, unjoin, provisioning, demotion, user/group and password administration,
ldap attribute modification, posix enablement, kdc timesync, pam and nss configuration,
daemon start/stop, cache flush, etc.
The ads command attempts to maintain compatibility with the proprietary vastool command,
while also adding additional features relevant to samba (such as kdc provisioning).

%prep
%setup -q

%build
autoreconf -if
%configure --prefix=%{_prefix} \
    --localstatedir=%{_localstatedir} \
    --sysconfdir=%{_sysconfdir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libdir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/ads

