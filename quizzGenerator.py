from abc import ABC, abstractmethod
from typing import List

class Question(ABC):
    @abstractmethod
    def print(self) -> None:
        """Print question."""
        pass
    
    @abstractmethod
    def check(self, string: str) -> bool:
        """Check given answer."""
        pass

class YesNoQuestion(Question):
    def __init__(self, string: str, boolean: bool) -> None:
        self.question = string
        self.answer = boolean  
    
    def print(self) -> None:
        print(f"[?] {self.question} (yes/no)")

    def check(self, string: str) -> bool:
        return (self.answer and string.lower() == 'yes') or (not self.answer and string.lower() == 'no')

class OpenQuestion(Question):
    def __init__(self, string: str, listOfStrings: List[str]) -> None:
        self.question = string
        self.answers = listOfStrings
    
    def print(self) -> None:
        print(f"[?] {self.question}")
    
    def check(self, string: str) -> bool:
        return string in self.answers

class MultiOptionsQuestion(Question):
    def __init__(self, string: str, listOfStrings: List[str], integer: int) -> None:
        self.question = string
        self.options = listOfStrings
        self.answer_index = integer
    
    def print(self) -> None:
        print(f"[?] {self.question}\n")
        for i in range(len(self.options)):
            print(f"[{i+1}] {self.options[i]}")
    
    def check(self, string: str) -> bool:
        try:
            ans = int(string)
            return ans == self.answer_index + 1
        except ValueError:
            return False

class Quiz:
    def __init__(self, questions: List[Question]) -> None:
        self.questions = questions
    
    def start(self) -> None:
        results = []
        for question in self.questions:
            question.print()
            ans = input("\n[+] ")
            is_correct = question.check(ans)
            results.append(is_correct)
            print("\n")
        self.print_results(results)
    
    def print_results(self, bools: List[bool]) -> None:
        points = sum(bools)
        n = len(bools)
        print(f"Your score is {points}/{n}\n")
        for i in range(1, n+1):
            if bools[i-1]:
                print(f"[{i}] Pass")
            else:
                print(f"[{i}] Fail")
