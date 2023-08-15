#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{

    char buffer[32];
    printf("address: %p\n", &buffer);
    strcpy(buffer, argv[1]);
    printf("buffer: %s\n", buffer);
    return 0;
}