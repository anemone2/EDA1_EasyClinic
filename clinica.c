// VERSION o.o.1 
// NO SE SI COMPILE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define LONGSTR 20

/*struct pac{

    int id;
    char nom[LONGSTR];
    int horario;
    int edad;
    int peso;

};*/

struct cita{

    int horario;
    
    char nom[LONGSTR];
    int edad;
    int peso;
    int precio;
    char doc[LONGSTR];
};

// Para vaciar una struct cita individual
struct cita citaVacia() {

    struct cita vacia;
    vacia.horario = 0;
    strcpy(vacia.nom, "Don XXXX");
    vacia.edad = 0;
    vacia.peso = 0;
    vacia.precio = 0;
    strcpy(vacia.doc, "Dr. XXXX");
    return vacia;
}

// Imprime el menu principal
int menu() {

    int opcionMenu;
    printf("* * MENU * *\n");
    printf("1. Paciente \n");
    printf("2. Administrador \n>> ");
    scanf("%d", &opcionMenu);
    return opcionMenu;
}

void printHorarios() {
    printf("* * QUE HORARIO DESEA * * \n");
    printf("1 - 07:00 a 08:00   7 - 12:00 a 13:00\n");
    printf("2 - 08:00 a 09:00   8 - 13:00 a 14:00\n");
    printf("3 - 09:00 a 10:00   9 - 14:00 a 15:00\n");
    printf("4 - 10:00 a 11:00  10 - 15:00 a 16:00\n");
    printf("5 - 11:00 a 12:00  11 - 16:00 a 17:00\n");
    printf("6 - 12:00 a 13:00  12 - 17:00 a 18:00\n");
    printf(">> ");
}

int main() {

    // Declaracion de variables
    int cuantos = 0; // Cantidad de pacientes 
    struct cita citas[12]; // Arreglo estatico de citas
    struct cita miCita; // Var auxiliar antes de asignarse al arreglo
    int miHorario=0;

    switch (menu())
    {
    case 1: // Menu de paciente

        cuantos++;

        printHorarios();
        scanf("%d", miHorario);
        
        printf("Nombre: ");
        fgets(citas[miHorario].nom, LONGSTR-1, stdin);
        printf("Edad: ");
        scanf("%d", citas[miHorario].edad);
        printf("Peso: ");
        scanf("%d", citas[miHorario].peso);
        printf("Precio: ");
        scanf("%d", citas[miHorario].precio);
        printf("Doctor: ");
        fgets(citas[miHorario].doc, LONGSTR-1, stdin);

        break;

    case 2: // Menu de administrador
        break;
    
    default:
        break;
    }

}

