# memory debug

## AddressSanitizer

1. build R on Linux with AddressSanitizer dynamic library

```
/root/r_source/R-4.1.0/configure CC="gcc -std=gnu99 -fsanitize=address,undefined,bounds-strict" CXX="g++ -fsanitize=address,undefined,bounds-strict -fno-omit-frame-pointer" CFLAGS="-fno-omit-frame-pointer -g -O2 -Wall -pedantic -mtune=native" --with-readline=no --with-x=no
make 
make install
```

2. run ```R CMD check``` with ```/root/r_source/R-4.1.0/bin/R```


## Valgrind

1. install Valgrind
2. run ```R CMD check --use-valgrind rDppDiversity-0.0.1.tag.gz```
