CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -g -O0
SRC = main.c tools/dict.c tools/char_list.c
OBJ = $(SRC:.c=.o)
TARGET = main.exe

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean