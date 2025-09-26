## 1. When the .py file task has the Parameter => ["--employee_name","Logeshwaran"]
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--employee_name", type=str, required=True)
args = parser.parse_args()
employee = args.employee_name
print("Total employee_name:", employee)
## Set taskValues
dbutils.jobs.taskValues.set('fullname', f'{employee}  S')