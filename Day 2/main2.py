from pathlib import Path
import json
import copy

dataset_path = Path(r"D:\Code Practice\Day 2\Dataset")

#To read the files from the folder and store it as nested dictionary 
def read_files_from_folder(dataset_path):
    all_file_data = {}
    for i in dataset_path.glob("task_*"):
        print(i.name)
        with open(i,"r") as file:
            file_content = json.load(file)
        all_file_data[i.name] = file_content
    return all_file_data

dataset = read_files_from_folder(dataset_path)
print(dataset)
print(len(dataset))

#To Determine the execution order
dataset_copy = copy.deepcopy(dataset) 

def order_of_execution(dataset_copy):
    execution_order = {}
    for key,values in dataset_copy.items():
        dataset_name = values["dataset_name"]
        executed_tasks = []
        tasks = values["tasks"]
        taskcount = values["task_count"]
        print(dataset_name)
        while(len(executed_tasks) < taskcount):
            for taskname, taskdetails in tasks.items():
                if(len(taskdetails["depends_on"]) == 0 and taskname not in executed_tasks):
                    executed_tasks.append(taskname)
                    for key, values in tasks.items():
                        if(taskname in values["depends_on"]):
                            values["depends_on"].remove(taskname)
            if len(executed_tasks) >= taskcount:
                break
        execution_order[dataset_name] = executed_tasks
    return execution_order

execution_order = order_of_execution(dataset_copy)
print(execution_order)
print(len(execution_order))
                
def simulation_of_execution(execution_order,dataset):
        for key, values in dataset.items():
            dataset_name = values["dataset_name"]
            tasks = values["tasks"]
            completed_tasks = []
            failed_tasks = []
            skipped_tasks = []
            count_of_completed_tasks = 0
            count_of_failed_tasks = 0
            count_of_skipped_tasks = 0
            print(dataset_name)
            for key, values in execution_order.items():
                if (key == dataset_name):
                    for taskname in values:
                        taskdetails = tasks[taskname]
                        status = taskdetails["should_fail"]
                        depends_on = taskdetails["depends_on"]
                        if any (task in failed_tasks or task in skipped_tasks for task in depends_on):
                            skipped_tasks.append(taskname)
                            count_of_skipped_tasks = count_of_skipped_tasks+1
                            print("[SKIPPED]", taskname)
                        else:
                            print("[RUNNING]",taskname)
                            if (status == False):
                                completed_tasks.append(taskname)
                                count_of_completed_tasks = count_of_completed_tasks + 1
                                print("[COMPLETED]", taskname)
                            elif(status == True):
                                failed_tasks.append(taskname)
                                count_of_failed_tasks = count_of_failed_tasks + 1
                                print("[FAILED]" , taskname)
            print("Dataset: " , dataset_name)
            print("Completed tasks:" , count_of_completed_tasks)
            print("Failed tasks: " , count_of_failed_tasks)
            print("Skipped tasks: ", count_of_skipped_tasks)
        return (count_of_completed_tasks, count_of_failed_tasks, count_of_skipped_tasks, completed_tasks, failed_tasks, skipped_tasks)
simulation = simulation_of_execution(execution_order,dataset)

