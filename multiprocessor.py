"""
I don't remember how this was supposed to work but it clearly doesn't work
also it wouldn't make much sense to run 3 simulations simultaneously
"""

import multiprocessing

workers = []

def worker1():
    exec(compile(open('animated_plotter.py').read(), 'animated_plotter.py', 'exec'))
workers.append(worker1)
    
def worker2():
    exec(compile(open('animator.py').read(), 'animator.py', 'exec'))
workers.append(worker2)

def testworker():
    print('testworker started')
workers.append(testworker)
    
if __name__ == '__main__':
    jobs = []
    for i in range(3):
        if i==0:
            continue
        p = multiprocessing.Process(target=workers[i])
        jobs.append(p)
        p.start()
    
