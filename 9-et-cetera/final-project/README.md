# TASKS APP

    #### Video Demo:  <URL HERE>
    #### Description:
    A simple task manager for getting things done where you can:
    - Add tasks
    - Remove tasks
    - Mark tasks as done
    - View your tasks list
    So all using Python's modules: sys, csv and os, no external libraries were used, and all accessible by simply using command-line arguments. Enjoy!

### The main function

Uses sys.argv to point to the point to the specified function and also handles any errors associated with argv. By default it calls show_help() which displays the options of flags, additionally you can use the -h flag to display the options.

### The add_tasks function

Before adding a task it checks if the tasks.csv file exists, this also can be changed as its decalared as a global variable. It prompts the user to write a task and its automatically assigned "False" in the "Done" column meaning its not done (yet) and appends it to the csv.

### The remove_tasks function

Reads the content or rather every row in tasks.csv and indexes the tasks starting from 1 then prompts the user for a task number to remove, then it removes the row/task from the csv file.

### The mark_task function

Prompts the user to input a task number if the csv file is not empty, then it check the "Done" value or rather string if its "True" it tells the user the task has already been marked done, otherwise it change the "Done" value from "False" to "True" and rewrite the updates task list in the csv.

### The show_tasks function

Using csv.DictReader it reads every task using headers, and then loops through each row of the tasks displaying both the task and the status, also handles errors or if the file is empty.
