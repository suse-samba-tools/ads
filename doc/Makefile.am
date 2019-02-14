
ads.1:
	argparse-manpage --pyfile=$(top_srcdir)/src/ads --function=argparser --author="David Mulder" --author-email="$(PACKAGE_BUGREPORT)" --project-name="$(PACKAGE)" --url="http://www.github.com/dmulder/ads" > $(srcdir)/$@
	sed -i 's/argparse-manpage/$(PACKAGE)/g' $(srcdir)/$@

man1_MANS = ads.1

CLEANFILES = ads.1
