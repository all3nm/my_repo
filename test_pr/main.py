from my_repo.test_pr.utils import greet
from my_repo.test_pr.config import APP_NAME

say = "Hello World 123!"

if __name__ == "__main__":
    print(greet(APP_NAME))
    print(say)