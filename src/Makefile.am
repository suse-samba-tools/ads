
adtool: adtool.in
	sed -e 's;[@]WINBINDD[@];$(prefix)/sbin/winbindd;g' -e 's;[@]KRB5CONF[@];$(sysconfdir)/krb5.conf;g' -e 's;[@]SMBD[@];$(prefix)/sbin/smbd;g' -e 's;[@]PAM_D[@];$(sysconfdir)/pam.d;g' -e 's;@WINBINDCONF@;$(sysconfdir)/security/pam_winbind.conf;g' -e 's;[@]LIBDIR[@];$(libdir);g' -e 's;[@]PYTHON[@];$(PYTHON);g' -e 's;[@]NSSWITCHCONF[@];$(sysconfdir)/nsswitch.conf;g' < $(srcdir)/adtool.in > $(srcdir)/adtool
	chmod +x adtool

bin_SCRIPTS = adtool

CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = adtool.in

