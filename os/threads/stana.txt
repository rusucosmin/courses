#include<stdio.h>
#include<pthread.h>
#include<string.h>
#include<stdlib.h>
/*
Implement a program that gets as arguments a file name followed by words. For each word, create a separate thread that counts its appearances in the given file.Print out the sum of the appearances of all words.
*/

int sum=0;
pthread_mutex_t mtx;

 struct csf 
{
	char* file;
	char* word;

};

int VerifyFile(const char* fName)
{
	FILE *file;
	if((file = fopen(fName,"r")))
	{
		fclose(file);
		return 1;
	}
	return 0;
}

void* MyThread(void* p)
{
	struct csf* ceva; 
     
	int number;
	char command[200];
	char line[100];
	char bla[100];
	FILE *fin;


        ceva = (struct csf*) p;

	snprintf(command,sizeof(command),"grep \"\\<%s\\>\" -o %s|wc -l",ceva->word,ceva->file);
	fin=popen(command,"r");
	fgets(line,1024,fin);
	strcpy(bla,line);
	number=atoi(bla);
	pclose(fin);
	
     pthread_mutex_lock(&mtx);
	sum+=number;		
     pthread_mutex_unlock(&mtx);	

	return NULL;
}

int main(int argc, char* argv[])
{
	pthread_t thr[argc];
	pthread_mutex_init(&mtx,NULL);
	
	struct csf argThread[argc];
	
	int i;
	if (VerifyFile(argv[1]) == 0)
	{
		printf("The first parameter is not a file\n");
		return 0;
	}
			
	for(i=2;i<argc;i++)
	{	

		argThread[i].file = (char*) malloc ( 20* sizeof(char));
		argThread[i].word = (char*) malloc (20 *sizeof(char));

		strcpy(argThread[i].file,argv[1]);
		strcpy(argThread[i].word,argv[i]);

		pthread_create(&thr[i],NULL,MyThread,(void*) &argThread[i]);
		
	}
	for(i=2;i<argc;i++)
	{
		pthread_join(thr[i],NULL);
	}

	for(i=2;i<argc;i++)
	{
		free(argThread[i].file);
		free(argThread[i].word);
	}

	pthread_mutex_destroy(&mtx);
	printf("%d\n",sum);
	return 0;
	
	

	
}
