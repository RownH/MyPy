myexe:a1.o a2.o b1.o b2.o
	cc -o myexe a1.o a2.o b1.o b2.o

a1.o:a1.c
	cc -c a1.c
a2.o:a2.c
	cc -c a2.c
b1.o:b1.c
	cc -c b1.c
b2.o:b2.c
	cc -c b2.c

clean:
	rm myexe a1.o a2.o b1.o b2.o
