#
# spec file for package adtool
#

Name:		adtool
Version:	0.9
Release:	1
License:	GPL-3.0
Summary:	Tool for working with ad users on samba/winbind
Url:		http://www.github.com/dmulder/adtool
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
Tool for working with ad users on samba/winbind

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
%{__install} -D -m 0755 src/adtool $RPM_BUILD_ROOT/%{_bindir}/adtool

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/adtool

