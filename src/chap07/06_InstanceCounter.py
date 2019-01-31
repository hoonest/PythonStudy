class InstanceCounter:
    counter = 0

    def __init__(self):
        InstanceCounter.counter += 1

    @classmethod
    def print_instance_count(cls):
        print(cls.counter)

if __name__ == '__main__':
    InstanceCounter.print_instance_count()
    a = InstanceCounter()
    InstanceCounter.print_instance_count()
    a.print_instance_count()
    InstanceCounter.print_instance_count()