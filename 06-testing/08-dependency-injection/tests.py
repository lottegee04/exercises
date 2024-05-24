from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub

def test_task_becomes_overdue():
    today = CalendarStub(date(2024,5,3))
    tomorrow = date.today() + timedelta(days=1)
    task = Task('do dishes', tomorrow)
    tasks = TaskList(today)
    
    tasks.add_task(task)
    assert tasks.overdue_tasks() == [task] 