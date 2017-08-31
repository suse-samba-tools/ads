#
# spec file for package adstool
#

Name:		adstool
Version:	0.9
Release:	1
License:	GPL-3.0
Summary:	Tool for working with ad users on samba/winbind
Url:		http://www.github.com/dmulder/adstool
Group:		Productivity/Networking/Samba
Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:   samba-client
Requires:   python-pam
Requires:   python-netifaces
Requires:   python-ldap
Requires:   krb5-client
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python

%description
Active Directory services tool for samba.
For join, unjoin, provisioning, demotion, user/group and password administration,
ldap attribute modification, posix enablement, kdc timesync, pam and nss configuration,
daemon start/stop, cache flush, etc.
The adstool command attempts to maintain compatibility with the proprietary vastool command,
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
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} -D -m 0755 src/adstool $RPM_BUILD_ROOT/%{_bindir}/adstool

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/adstool

