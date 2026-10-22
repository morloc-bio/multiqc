.PHONY: all test clean

all: test

test:
	morloc make -o test-multiqc test/main.loc
	./test-multiqc | tee test.out
	tail -n 1 test.out | grep -qx true

clean:
	rm -rf test-multiqc test-multiqc-build test.out
