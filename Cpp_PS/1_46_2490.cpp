#include <stdio.h>
int main() {
	int in, front=0;
	for (int i = 0; i < 3; i++, front=0) {
		for (int j = 0; j < 4; j++) {
			scanf_s("%d", &in);
			if (in == 0 ) front++;
		}
		switch (front){
		case 0: printf("E\n"); break;
		case 1: printf("A\n"); break;
		case 2: printf("B\n"); break;
		case 3: printf("C\n"); break;
		case 4: printf("D\n"); break;
		}
	}
}