import threading
import time
import random


class LoginManager:
    def __init__(self):
        self.is_logged_in = False
        self.stop_event = threading.Event()
        self.login_condition = threading.Condition()
        self.login_failed_condition = threading.Condition()

    def check_login(self):
        while not self.stop_event.is_set():
            # Simulate a login check
            time.sleep(10)  # Check every 10 seconds
            if self.successful_login_check():
                with self.login_condition:
                    self.is_logged_in = True
                    self.login_condition.notify_all()
                    print("Login successful.")
            else:
                with self.login_failed_condition:
                    self.is_logged_in = False
                    self.login_failed_condition.notify_all()
                print("Login failed. Retrying in 10 seconds...")

    def successful_login_check(self):
        # Simulate a successful login check (return True or False based on your logic)
        return random.randint(1, 10) > 3


class MainTask:
    def __init__(self, login_manager):
        self.login_manager = login_manager

    def run(self):
        while not self.login_manager.stop_event.is_set():
            with self.login_manager.login_condition:
                while not self.login_manager.is_logged_in:
                    print("Main task: Waiting for login to be successful.")
                    self.login_manager.login_condition.wait()
                    if self.login_manager.stop_event.is_set():
                        break

                if not self.login_manager.is_logged_in:
                    continue  # Exit the loop if login failed

                print("Main task: User is logged in, performing main task.")
                self.do_something()

    def do_something(self):
        time.sleep(20)  # Simulate a 20-second task
        print("Main task: After sleep 20 seconds.")

    def wait_login_failed(self):
        with self.login_manager.login_failed_condition:
            while not self.login_manager.is_logged_in:
                print("Main task: Login failed. Waiting for 15 minutes...")
                self.login_manager.login_failed_condition.wait(timeout=60)  # Wait for 15 minutes (900 seconds)


if __name__ == "__main__":
    login_manager = LoginManager()
    check_login_thread = threading.Thread(target=login_manager.check_login)

    main_task = MainTask(login_manager)
    main_task_thread = threading.Thread(target=main_task.run)
    wait_login_failed_thread = threading.Thread(target=main_task.wait_login_failed)

    check_login_thread.start()
    main_task_thread.start()
    wait_login_failed_thread.start()

    try:
        check_login_thread.join()
        main_task_thread.join()
        wait_login_failed_thread.join()
    except KeyboardInterrupt:
        # Handle Ctrl+C to gracefully stop the threads
        login_manager.stop_event.set()
