import unittest
from task_list import add_task,remove_task,mark_complete,view_tasks

class test_add_task(unittest.TestCase):

    def setUp(self):
        # This will run before every test. We'll use it to initialize a fresh task list.
        self.task_list= []

    def test_add_task(self):
        # Add a task and check if it's in the list
        add_task(self.task_list, "Task 1")
        self.assertIn("Task 1", self.task_list)
        self.assertEqual(len(self.task_list), 1)  # Ensure there's exactly 1 task in the list

# needs debug
#    def test_view_tasks(self): 
        # Add tasks and then check if view_tasks returns the correct list
 #      add_task(self.task_list, "Task 1")
  #     add_task(self.task_list, "Task 2")
   #    self.assertEqual(view_tasks(self.task_list), ["Task 1", "Task 2"])

    def test_remove_task(self):
        # Add tasks, remove one, and check if it was removed
        add_task(self.task_list, "Task 1")
        add_task(self.task_list, "Task 2")
        remove_task(self.task_list, 1)  # Remove the first task
        self.assertNotIn("Task 1", self.task_list)
        self.assertEqual(len(self.task_list), 1)  # Ensure only 1 task is left

 #function not implemented yet.    
    def test_mark_complete(self):
        # Add tasks, mark one as complete, and check if it was removed
        add_task(self.task_list, "Task 1")
        add_task(self.task_list, "Task 2")
        mark_complete(self.task_list, 2)  # Mark the second task as complete
        self.assertNotIn("Task 2", self.task_list)
        self.assertEqual(len(self.task_list), 1)  # Ensure only 1 task remains

if __name__ == '__main__':
    unittest.main()