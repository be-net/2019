
all:
	cd src && $(MAKE)
	hugo --cleanDestinationDir
	@tree docs
