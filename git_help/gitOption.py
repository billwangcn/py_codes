
import os,sys

#print(keywords)
#os.getcwd()
#os.system('git push --help >> git_push_help.txt')

def commandHelp():
    keywords=['clone','init','add',
    'mv',
    'reset',
    'rm',
    '',
    'bisect',
    'grep',
    'log',
    'show',
    'status',
    '',
    'branch',
    'checkout',
    'commit',
    'diff',
    'merge',
    'rebase',
    'tag',
    '',
    'fetch',
    'pull',
    'push',]
    #print(keywords)
    
    for i in keywords:
        c2help(i)
    # if len(i)>0: 
    #     print(i)
    #     cmd='git %s --help >> git_%s_help.md'%(i,i)
    #     os.system(cmd)


def c2help(i):
        if len(i)>0:
                print(i)
                vcmd='git %s --help >> git_%s_help.md'%(i,i)
                os.system(vcmd)  


if __name__ == "__main__":
    c2help('remote')
    pass