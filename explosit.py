#!/bin/python3
import sys
import argparse
import threading
import multiprocessing
import webbrowser
import socket
import socketserver
import http
import math
import cmath

def argsp():
    parser = argparse.ArgumentParser(description='Explosit it is a server that helps in pentesting assessments.')
    parser.add_argument('--init', action='store_true')
    parser.add_argument('--close', action='store_true')

    return parser.parse_args()

def init_explosit():
    print("[+] explosit adversary active")

def close_explosit():
    print("[-] explosit adversary inactive")

def main():
    args = argsp()
    if args.init and not args.close:
        init_explosit()
    elif args.close and not args.init:
        close_explosit()

if __name__ == "__main__":
   main()