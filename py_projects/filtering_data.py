from data import DATA

def run():

    all_python_devs = [i["name"]  for i in DATA  if i["language"] == "python" ]
    for i in all_python_devs: 
        print(f"devs: {i}")

    all_python_devsX = list(filter(lambda i: i["language"] == "python"  , DATA))
    all_python_devsX = list(map(lambda i: i["name"], all_python_devsX))
    for i in all_python_devsX: 
        print(f"-devsX: {i}")

    all_google_workers = [i["age"] for i in DATA if i["organization"] == "Google"]
    for i in all_google_workers: 
        print(f"google: {i}")

    all_google_workersX = list(filter(lambda i: i["organization"] == "Google" , DATA))
    all_google_workersX = list(map(lambda i: i["age"], all_google_workersX))
    for i in all_google_workersX: #OR all_googler_workers:
        print(f"-googleX: {i}")


    #///////////////////////////////////////
    print("\n\n") 
    #///////////////////////////////////////


    adults = list(filter(lambda i: i["age"] > 18 , DATA))
    adults = list(map(lambda i: i["age"] , adults))
    for i in adults:
        print(f"adults: {i}")
    
    adultsX = [i["age"]  for i in DATA  if i["age"] > 18]
    for i in adultsX:
        print(f"-adultsX: {i}")

    old_people = list(map(lambda i: i | {"old": i["age"] > 70}, DATA))
    for i in old_people:
        print(f"old_people: {i}")
    
    old_peopleX = [i["age"]  for i in DATA  if i["age"] > 70]
    for i in old_peopleX:
        print(f"-old_peopleX: {i}")

if __name__ == "__main__":
    run()