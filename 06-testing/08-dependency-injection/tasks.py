from datetime import date, timedelta
class Task:
    def __init__(self, description,due_date ):
        
        self.__description= description
        self.__due_date = due_date
        self.finished = False
    
    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def finished(self):
        return self.__finished
    
    
    @finished.setter
    def finished(self, value):
        self.__finished = value
    
class TaskList:
    def __init__(self,calendar):
        self.__task_list = []
        self.__calendar =calendar
        
    
    @property
    def calendar(self):
        return self.__calendar
    
    @property
    def task_list(self):
        return self.__task_list
    
    def add_task(self,task):
        if task.due_date < self.calendar.today:
            raise RuntimeError
        else:
            self.task_list.append(task)
    
    def finished_tasks(self):
        return [task for task in self.task_list if task.finished]
    
    def due_tasks(self):
        return [task for task in self.task_list if task.finished == False]
    
    def overdue_tasks(self):
        return [task for task in self.task_list if task.finished == False and task.due_date > self.calendar.today]