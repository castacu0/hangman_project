from data import DATA

def run():
    """
    In this example, I'm using List comprehensions (first two), and 
    two lambda techniques with map and filter to have a similar result
    """

    all_python_devs = [i["name"]  for i in DATA  if i["language"] == "python" ]
    for i in all_python_devs: 
        print(f"devs: {i}")

    all_google_workers = [i["age"] for i in DATA if i["organization"] == "Google"]
    for i in all_google_workers: 
        print(f"google: {i}")
        

    adults = list(filter(lambda i: i["age"] > 18 , DATA))
    adults = list(map(lambda i: i["age"] , adults))
    for i in adults:
        print(f"adults: {i}")

    old_people = list(map(lambda i: i | {"old": i["age"] > 70}, DATA))
    for i in old_people:
        print(f"old_people: {i}") 

if __name__ == "__main__":
    run()