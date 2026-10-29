#include <stdio.h>
#include <io.h>

struct logs{
    char testname [120];
    char status [10];
    double executiontime;
};

#To read the dataset folder and store it as 

char dataset_path [] = "D:\\Code Practice\\Day 1\\Dataset"

int main(void){
    sturct _finddata_t ;
    first_search = _findfirst("D:\Code Practice\Day 1\Dataset\test_*, &entry");

    if(first_search == -1){
        printf("No Files found");
    }
    else{
        printf("Filename : %s\n" , entry.name);
        FILE* file = fopen(entry.name, "r");
        if(file != NULL){
            fgets(line)
            printf("%s",line);
        }
        fclose(file);
    }
}


struct log_extraction_from_file(all_logs){
    all_logs = {}
    for i in dataset_path(find_data){
        list_of_dict = [];
        print(i.name)
        file_content = FILE *file = fopen(i.name, "r");
        for j in file_content{
            parts = j.strip().split(":")
            one_file_dict={
                    "testname": parts[0],
                    "status": parts[1],
                    "execution_time":float(parts[2])
            }
        }
        list_of_dict.append(one_file_dict)
    }
    return all_logs
}

