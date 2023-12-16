# Use the filter() function to remove all the undone tasks from the tasks list and print the new list on the console.
tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]

def filter_tasks(task):
    return task["done"] == True

resulting_tasks = list(filter(filter_tasks, tasks))
print(resulting_tasks)

# same as above but with lambda
resulting_tasks = list(filter(lambda task: task["done"] == True, tasks))
print(resulting_tasks)

# same as above but with list comprehension
resulting_tasks = [task for task in tasks if task["done"] == True]
print(resulting_tasks)