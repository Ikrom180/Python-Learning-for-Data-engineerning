# I - Interface Segregation Principle
# Don't force a class to implement methods it doesn't need.


# BAD Example (Violating I):

# Fat interface - forces everything
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# Human can do all three
class Human(Worker):
    def work(self):
        return "Human working"

    def eat(self):
        return "Human eating"

    def sleep(self):
        return "Human sleeping"


# Robot only works - but is FORCED to implement eat and sleep!
class Robot(Worker):
    def work(self):
        return "Robot working"

    def eat(self):
        # ❌ PROBLEM: Robots don't eat!
        # Forced to write a fake, empty method
        return None  # Does nothing

    def sleep(self):
        # ❌ PROBLEM: Robots don't sleep!
        return None  # Does nothing

    # The Robot class is forced to implement eat() and sleep()
    #
    # It
    # has
    # empty / fake
    # methods
    # that
    # do
    # nothing
    #
    # If
    # someone
    # calls
    # robot.eat(), they
    # 'd expect eating behavior but get nothing!

    # Step 1: Split into SMALL, specific interfaces
    class Workable:
        def work(self):
            pass

    class Eatable:
        def eat(self):
            pass

    class Sleepable:
        def sleep(self):
            pass

    # Step 2: Classes implement ONLY what they need
    class Human(Workable, Eatable, Sleepable):
        def work(self):
            return "Human working"

        def eat(self):
            return "Human eating"

        def sleep(self):
            return "Human sleeping"

    class Robot(Workable):
        # ✅ Robot ONLY implements work
        # No fake methods needed!
        def work(self):
            return "Robot working"

    # Step 3: Functions work with specific interfaces
    def start_work(worker: Workable):
        print(worker.work())

    def lunch_break(eater: Eatable):
        print(eater.eat())

    # Testing
    human = Human()
    robot = Robot()

    start_work(human)  # ✅ Works!
    start_work(robot)  # ✅ Works!
    lunch_break(human)  # ✅ Works!
    # lunch_break(robot)  # ❌ This would give a TYPE ERROR (robot can't eat)