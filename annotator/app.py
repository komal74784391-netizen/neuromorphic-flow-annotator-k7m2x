import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', required=True)
    args = parser.parse_args()
    print('opening annotation canvas for', args.dataset)


if __name__ == '__main__':
    main()
