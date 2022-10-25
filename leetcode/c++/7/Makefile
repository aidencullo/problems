target	:= output
objs	:= main.o solution.o

CPP	:= gcc
CFLGAS	:= -Wall -Werror

all: $(target)

dep	:= $(pathsub %.o,%.d,$(objs))
-include $(deps)
DEPFLAGS = -MMD -MF $(@:.o=.d)

output: $(objs)
	$(CPP) $(CFKAGS) -o $@ $^

%.o: %.cpp
	$(CPP) $(CFKAGS) -c $< $(DEPFLAGS)

clean:
	rm $(target) $(objs) *~ \#*\#
