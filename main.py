from pathlib import Path

dataset_path = Path(r"D:\Code Practice\Day 1\Dataset")

#To read the file from the dataset folder and store it as a Dictionary of Lists of Dictionaries
def read_files_from_dataset(dataset_path):
    all_logs={}

    for i in dataset_path.glob("test_*"):
        list_of_dict = []
        #print(i.name)
        with open(i , "r") as file:
            file_content = file.readlines()
            for j in file_content:
                parts = j.strip().split(":")
                one_file_dict={
                    "testname": parts[0],
                    "status": parts[1],
                    "execution_time":float(parts[2])
                }
                list_of_dict.append(one_file_dict)
        all_logs[i.name] = list_of_dict
    return all_logs

logs = read_files_from_dataset(dataset_path)
#print(logs)
#print(len(logs))

#To find the total number of passed and failed tests
def count_of_status(logs):
    for name, list in logs.items():
        count_of_pass = 0
        count_of_fail = 0
        for i in list:
            if(i["status"]=="PASS"):
                count_of_pass = count_of_pass+1
            elif(i["status"] == "FAIL"):
                count_of_fail = count_of_fail+1
        total_number_testcases = count_of_pass + count_of_fail
        #print("Filename: ", name)
        #print("Number of Test Case passed: ", count_of_pass)
        #print("Number of Test Case failed: ", count_of_fail)
        #print("Total number of Test Case: ", total_number_testcases)
    return count_of_pass, count_of_fail

num_of_pass_fail = count_of_status(logs)

#To find the average execution time
def avg_execution_time(logs):
    for name, list in logs.items():
        tot_execution_time = 0
        for i in list:
            execution_time = i["execution_time"]
            tot_execution_time = tot_execution_time + execution_time
            avg_execution_time = tot_execution_time/len(list)
        #print("Filename: ", name)
        #print("Average execution time is: ", avg_execution_time)
    return avg_execution_time

average_execution_time = avg_execution_time(logs)

#To find the test with the highest execution time
def highest_execution_time(logs):
    for name, list in logs.items():
        high_execution_time = 0
        for i in list:
            if(i["execution_time"]>high_execution_time):
                high_execution_time = i["execution_time"]
                high_execution_time_testcase = i["testname"]
        #print("Filename: ", name)
        #print("The Test with highest execution time is: ", high_execution_time_testcase)
        #print("The execution time of the test case is: ", high_execution_time)
    return(high_execution_time, high_execution_time_testcase)

slowest_test = highest_execution_time(logs)

#To find the flaky tests
def find_flaky_tests(logs):
    for name, list in logs.items():
        pass_count = {}
        fail_count = {}
        test_name = {}
        for i in list:
            if(i["testname"] not in test_name):
                test_name[i["testname"]] = i["testname"]
                pass_count[i["testname"]] = 0
                fail_count[i["testname"]] = 0
            if(i["status"] == "PASS"):
                pass_count[i["testname"]] = pass_count[i["testname"]]+1
            elif(i["status"] == "FAIL"):
                fail_count[i["testname"]] = fail_count[i["testname"]]+1
        #for i in test_name:
            #if(pass_count[i] > 0 and fail_count[i]> 0):
                #print("Filename: ", name)
                #print({test_name[i]: {
                #    "PASS": pass_count[i],
                #    "FAIL": fail_count[i]
                #}})
    return(test_name, pass_count,fail_count)

flaky_test_name = find_flaky_tests(logs)

#To store the report in the file as well as to print in the terminal
def print_summary(logs):
    report_path = dataset_path.parent / "report"

    if not report_path.exists():
        report_path.mkdir()
    for name, list in logs.items():
        count_of_pass, count_of_fail = count_of_status({name:list})
        average_execution_time = avg_execution_time({name:list})
        high_execution_time, high_execution_time_testcase = highest_execution_time({name:list})
        test_name, pass_count, fail_count = find_flaky_tests({name:list})
        total_number_testcases = count_of_pass + count_of_fail
        report = [
            f"Total tests: {total_number_testcases}",
            f"Passed: {count_of_pass}",
            f"Failed: {count_of_fail}",
            f"Average execution time: {average_execution_time:.2f} seconds",
            f"Slowest test: {high_execution_time_testcase} ({high_execution_time} seconds)",
            "",
            "Test Summary:"
        ]
        for i in test_name:
            report.append(
                f"{test_name[i]} -> Passed: {pass_count[i]}, Failed: {fail_count[i]}"
            )
        report.extend(["", "Flaky tests:"])
        for i in test_name:
            if pass_count[i] > 0 and fail_count[i] > 0:
                report.append(test_name[i])
        report_content = "\n".join(report)
        print(f"\nReport for {name}")
        print(report_content)
        report_file = report_path / f"report_{Path(name).stem}.txt"
        with open(report_file, "w", encoding="utf-8") as file:
            file.write(report_content)

summary = print_summary(logs)

    
        




