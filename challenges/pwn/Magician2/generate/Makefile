CC = gcc
NAME = magic2
CFLAGS = -fno-stack-protector -z execstack -no-pie -m32

all:
	$(CC) ${NAME}.c $(CFLAGS) -o ../service/${NAME}-server
	$(CC) ${NAME}.c $(CFLAGS) -o ../distrib/${NAME}-distrib
	cp $(NAME).c ../distrib/$(NAME).c
	
clean:
	rm ../service/${NAME}*
	rm ../distrib/${NAME}*
