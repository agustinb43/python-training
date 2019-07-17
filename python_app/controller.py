from python_app.service import Service

class Controller(object):
    """TO-DO Controller"""

    def __init__(self):
        self.service = Service()

    def get_todos(self):
        all_todos = self.service.list_todos()
        rows_to_return = "TO-DOS: \n"
        for row in all_todos:
            rows_to_return = rows_to_return + row[0] 
            rows_to_return = rows_to_return + "\n"
        print(rows_to_return)
        return rows_to_return

    def add_todo(self, todo):
        print("Adding new TODO {0}".format(todo))
        self.service.add_todo(todo)
        return "Todo saved!"