#!/bin/python3
import sys
import requests
import argparse

def argsp()
    parser = argparse.ArgumentParser(description='Calculadora, suma/resta/multiplica a y b')
    parser.add_argument('--init', action='store_true')
    parser.add_argument('--close', action='store_true')


    return parser.parse_args()

def init_explosit():
    print("explosit adversari active")

def close_explosit():
    print("explosit adversari inactive")

def main():
    args = argsp()
    if args.init and not args.close:
        init_explosit()
    elif args.close and not args.init:
        close_explosit()

if __name__ == "__main__":
   main()