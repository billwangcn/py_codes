


import os,sys

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

#os.getcwd('git push --help >> git_push_help.txt')
#os.system('git push --help >> git_push_help.txt')

for i in keywords:
    if len(i)>0: 
        print(i)
        cmd='git %s --help >> git_%s_help.md'%(i,i)
        os.system(cmd)