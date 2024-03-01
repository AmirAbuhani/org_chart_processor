# Amir Abu Hani
import json


# Read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Define function to count all the workers in each company
def count_workers(company):
    if 'subordinates' not in company:
        # Base case: if the company has no subordinates, return 1 (counting the CEO as 1 worker)
        return 1
    else:
        # Recursive case: count workers in each subordinate department or team
        total_workers = 1  # Count the CEO
        for subordinate in company['subordinates']:
            total_workers += count_workers(subordinate)
        return total_workers


# Define function to count workers under the CTO
def count_workers_under_cto(company):
    if 'subordinates' in company:
        for subordinate in company['subordinates']:
            if subordinate['name'] == 'CTO':
                return count_workers(subordinate)
    return 0


# Define function to count workers with developer in their title
def count_workers_with_developer_title(company):
    count = 0
    if 'subordinates' in company:
        for subordinate in company['subordinates']:
            # Check if the current subordinate's name contains "Developer"
            if 'Developer' in subordinate['name']:
                # If yes, increment the count
                count += 1
            # Recursively count workers from subordinates
            count += count_workers_with_developer_title(subordinate)
    return count


# Define function to count the departments in each company
def count_departments(company):
    if 'subordinates' not in company:
        # Base case: if the company has no subordinates, return 0
        return 0
    else:
        # Recursive case: count departments in each subordinate department or team
        total_departments = 1  # Count the current department
        for subordinate in company['subordinates']:
            total_departments += count_departments(subordinate)
        return total_departments


# Read JSON data from companies file
json_file_path = 'companies.json'
json_data = read_json_file(json_file_path)

org_chart_large = json_data['org_chart_large']
tech_company_org_chart_2 = json_data['tech_company_org_chart_2']
tech_company_org_chart_3 = json_data['tech_company_org_chart_3']

# Count workers in each company
org_chart_large_workers = count_workers(org_chart_large)
tech_company_org_chart_2_workers = count_workers(tech_company_org_chart_2)
tech_company_org_chart_3_workers = count_workers(tech_company_org_chart_3)
print("org_chart_large workers:", org_chart_large_workers)
print("tech_company_org_chart_2 workers:", tech_company_org_chart_2_workers)
print("tech_company_org_chart_3 workers:", tech_company_org_chart_3_workers)
print()

# Count workers under the CTO in each company
org_chart_large_workers_under_cto = count_workers_under_cto(org_chart_large)
tech_company_org_chart_2_workers_under_cto = count_workers_under_cto(tech_company_org_chart_2)
tech_company_org_chart_3_workers_under_cto = count_workers_under_cto(tech_company_org_chart_3)
print("Number of workers under the CTO in org_chart_large:", org_chart_large_workers_under_cto)
print("Number of workers under the CTO in tech_company_org_chart_2:", tech_company_org_chart_2_workers_under_cto)
print("Number of workers under the CTO in tech_company_org_chart_3:", tech_company_org_chart_3_workers_under_cto)
print()

# count workers with developer in their title in each company
org_chart_large_developers = count_workers_with_developer_title(org_chart_large)
tech_company_org_chart_2_developers = count_workers_with_developer_title(tech_company_org_chart_2)
tech_company_org_chart_3_developers = count_workers_with_developer_title(tech_company_org_chart_3)
print("Number of developers in org_chart_large: ", org_chart_large_developers)
print("Number of developers in tech_company_org_chart_2: ", tech_company_org_chart_2_developers)
print("Number of developers in tech_company_org_chart_3: ", tech_company_org_chart_3_developers)
print()

# count departments in each company
org_chart_large_departments = count_departments(org_chart_large)
tech_company_org_chart_2_departments = count_departments(tech_company_org_chart_2)
tech_company_org_chart_3_departments = count_departments(tech_company_org_chart_3)
print("Number of departments in org_chart_large: ", org_chart_large_departments)
print("Number of departments in tech_company_org_chart_2: ", tech_company_org_chart_2_departments)
print("Number of departments in tech_company_org_chart_3: ", tech_company_org_chart_3_departments)
