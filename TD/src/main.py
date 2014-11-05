# Import from existence package
from existence import Existence010


def main():
    existence = Existence010()

    for i in range(0, 20):
        step_trace = existence.step()
        print('{0}: {1}'.format(i, step_trace))

if __name__ == '__main__':
    main()
