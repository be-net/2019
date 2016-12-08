
all:
	cd src && $(MAKE)
	cd ./book_of_abstract && $(MAKE)
	hugo --cleanDestinationDir
