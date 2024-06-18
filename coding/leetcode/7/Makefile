target	:= output
objs	:= main.o solution.o

CC	:= gcc -std=gnu11
CPP	:= g++ -std=c++17
# 02 suggest optimizations
# -pipe avoids temp files
# -fwrapv detects signed interger overflow
# -Werror make all warnings errors
CFLAGS	:= -Wall -Werror -fwrapv -O2 -pipe

all: $(target)

dep	:= $(pathsub %.o,%.d,$(objs))
-include $(deps)
DEPFLAGS = -MMD -MF $(@:.o=.d)

output: $(objs)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.cpp
	$(CPP) $(CFLAGS) -c $< $(DEPFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< $(DEPFLAGS)

clean:
	rm $(target) $(objs) *~ \#*\#
