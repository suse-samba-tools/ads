
ads: ads.in
	sed -e 's;[@]VERSION[@];$(PACKAGE_STRING);g' < $(srcdir)/ads.in > $(srcdir)/ads
	chmod +x ads

bin_SCRIPTS = ads vastool

CLEANFILES = ads
EXTRA_DIST = ads.in

