#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

typedef uint8_t BYTE;

void checkArgumentCount(int argc);
void checkFileExists(FILE *file);
int isJPEG(BYTE buffer[]);

int main(int argc, char *argv[])
{
    checkArgumentCount(argc);
    FILE *raw = fopen(argv[1], "r");
    checkFileExists(raw);

    BYTE buffer[BLOCK_SIZE];

    char filename[8];
    FILE *image;
    int counter = 0;

    while (fread(buffer, BLOCK_SIZE, 1, raw) == 1)
    {
        if (isJPEG(buffer) == 1)
        {
            if (counter != 0)
            {
                fclose(image);
            }
            sprintf(filename, "%03i.jpg", counter++);
            image = fopen(filename, "w");
            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
        else if (counter > 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
    }
    fclose(raw);
    fclose(image);
}

void checkArgumentCount(int argc)
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        exit(1);
    }
}

void checkFileExists(FILE *file)
{
    if (file == NULL)
    {
        printf("File could not be opened.\n");
        exit(1);
    }
}

int isJPEG(BYTE buffer[])
{
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        return 1;
    }
    return 0;
}
