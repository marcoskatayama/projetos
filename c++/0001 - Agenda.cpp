#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

struct agenda
{
	int codigo;
	char nome[30];
	char email[30];
	int telefone;
};

int main()
{
	setlocale(LC_ALL, "Portuguese");

	struct agenda a[5];

	int sair;
	int menu;
	int codigoCliente = 0;
	int i = 0;
	
	do
	{
		
		int novoCadastro = 1;
		printf("\n-----------------------------------\n");
		printf("              AGENDA\n");
		printf("-----------------------------------\n\n");
		printf("1 – Inserir um novo cadastro\n");
		printf("2 – Mostrar todos os cadastros\n");
		printf("0 – Encerrar\n");
		printf("\n------------------------------------\n");
		printf("Escolha a opção: ");
		fflush(stdin);
		scanf("%d", &menu);
		system("cls");

		switch(menu)
		{
		case (1):
			
			while(codigoCliente < 5 && novoCadastro == 1)
			{
				printf("\n------------------------------------\n");
				printf("           NOVO CADASTRO\n");
				printf("------------------------------------\n\n");

				codigoCliente++;
				a[i].codigo = codigoCliente;
				printf("Codigo: %d\n", a[i].codigo);

				printf("Nome: ");
				fflush(stdin);
				gets(a[i].nome);

				printf("Email: ");
				fflush(stdin);
				gets(a[i].email);

				printf("Telefone: ");
				fflush(stdin);
				scanf("%d", &a[i].telefone);
				
				i++;

				printf("\nDeseja fazer novo cadastro?\n");
				printf("1-Sim ou 2-Não\n");
				fflush(stdin);
				scanf("%d", &novoCadastro);
				system("cls");
			}
			
			if(codigoCliente >= 5){
				printf("\n------------------------------------\n");
				printf("             AGENDA LOTADA!\n");
				printf("------------------------------------\n\n");
				system("pause");
			}
			
			system("cls");

			break;

		case (2):

			i = 0;

			printf("\n------------------------------------\n");
			printf("             CLIENTES\n");
			printf("------------------------------------\n\n");
			
			while(i < codigoCliente)
			{
				printf("Codigo: %d\n", a[i].codigo);
				printf("Nome: %s\n", a[i].nome);
				printf("Email: %s\n", a[i].email);
				printf("Telefone: %d\n", a[i].telefone);
				printf("---------------------------------------\n");

				i++;
			}

			system("pause");
			system("cls");

			break;
		
		case(0):
	
			sair = 1;
					
        	break;
        
		default:
			
			printf("\n------------------------------------\n");
			printf("         ERRO: OPÇÃO INVALIDA!\n");
			printf("------------------------------------\n\n");
			system("pause");
			system("cls");
			
			break;
		}

	}
	while(sair != 1);

	printf("\n------------------------------------\n");
	printf("             FIM DO PROGRAMA\n");
	printf("------------------------------------\n\n");
}
