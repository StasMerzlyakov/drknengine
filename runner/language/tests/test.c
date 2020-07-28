#include <stdio.h>
#include "test.h"

#define btoa(x) ((x)?"true":"false")

void method1(int val) {
    printf("method1 %d\n",val);
}

int method2(bool val){
    printf("method2 %s\n",btoa(val));
    return 1;
}

void method3(int val) {
    printf("method3 %d\n",val);
}

void gett(){
    printf("gett\n");
}

void gett2(){
    printf("gett2\n");
}

