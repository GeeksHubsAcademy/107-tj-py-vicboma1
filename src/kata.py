import shlex
import sys


#
# Apply Method
# @param input
# @return
#    
def apply(input):
    #your code here
    return input;

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply(["2","2"]))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 
