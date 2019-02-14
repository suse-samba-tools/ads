
ads: ads.in
	sed -e 's;[@]KRB5CONF[@];$(sysconfdir)/krb5.conf;g' -e 's;[@]PAM_D[@];$(sysconfdir)/pam.d;g' -e 's;@WINBINDCONF@;$(sysconfdir)/security/pam_winbind.conf;g' -e 's;[@]LIBDIR[@];$(libdir);g' -e 's;/usr/bin/python;$(PYTHON);g' -e 's;[@]NSSWITCHCONF[@];$(sysconfdir)/nsswitch.conf;g' -e 's;[@]BINDIR[@];$(bindir);g' -e 's;[@]SBINDIR[@];$(sbindir);g' -e 's;[@]VERSION[@];$(PACKAGE_STRING);g' < $(srcdir)/ads.in > $(srcdir)/ads
	chmod +x ads

bin_SCRIPTS = ads

CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = ads.in

