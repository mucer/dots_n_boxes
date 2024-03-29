
all : catch2

src/lib/catch2.tar.gz :
	mkdir -p src/lib
	wget https://github.com/catchorg/Catch2/archive/v3.5.2.tar.gz -O src/lib/catch2.tar.gz

.PHONY : catch2
catch2 : src/lib/catch2.tar.gz
	mkdir -p src/lib/Catch2
	tar -C src/lib/Catch2 --strip-components=1 -xf src/lib/catch2.tar.gz


.PHONY : clean
clean :
	rm src/lib/catch2.tar.gz
	rm -rf src/lib/Catch2