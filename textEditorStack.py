import unittest

class TextOperation:
    def __init__(self, type: str, character: str) -> None:
        self.type = type
        self.character = character

class Operations:
    def __init__(self) -> None:
        self.operations = []
        self.test_str = ''
    
    def add(self, character):
        add_operation = TextOperation("add", character)
        self.operations.append(add_operation)
        self.test_str += character

    def delete(self):
        delete_operation = TextOperation("delete", self.test_str[-1])
        self.operations.append(delete_operation)
        self.test_str = self.test_str[:-1]
        
    def undo(self):
        top = self.operations.pop(-1)
        if top.type == 'add':
            self.test_str = self.test_str[:-1]
        elif top.type == 'delete':
            self.test_str += top.character


class TestUndo(unittest.TestCase):
    def test_add(self):
        undo = Operations()
        undo.add('a')
        print(undo.operations[-1].type)
        undo.add('b')
        undo.add('c')
        undo.add('d')
        # print(undo.test_str)
    
    def test_delete(self):
        undo = Operations()
        undo.add('a')
        undo.add('a')
        undo.delete()
        print(undo.operations[-1].type)
        print(undo.test_str)

    def test_undo(self):
        undo = Operations()
        undo.add('a')
        undo.add('a')
        undo.undo()
        print(undo.test_str)

if __name__ == "__main__":
    unittest.main()