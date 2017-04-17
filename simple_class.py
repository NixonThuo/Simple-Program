class Bootcamp(object):
    tasks = {1: "TDD", 2: "OOP", 3: "Programming Logic", 4:
             "Version Control", 5: "Agile Methodology",
             6: "Growth Mindset", 7: "Asking Questions", 8:
             "Motivation and Commitment", 9: "Speaking"}

    def __init__(self, name, tasks=tasks):
        self.name = name
        self.tasks = tasks
        self.completed = []
        self.incompleted = tasks.values()

    def add_completed_items(self, i):
        if i in self.tasks.keys():
            self.completed.append(self.tasks[i])
            self.incompleted.remove(self.tasks[i])
            return "tasks added to complete"
        else:
            return "not in the tasks"

    def check_progress(self):
        self.progress = float(len(self.completed)) / \
            float(len(self.tasks)) * 100
        return int(self.progress)


nick = Bootcamp("nick")
print nick.tasks
print nick.add_completed_items(1)
print nick.add_completed_items(2)
print nick.add_completed_items(3)
print nick.incompleted
print nick.completed
print nick.check_progress()
