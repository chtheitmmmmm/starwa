if __name__ == '__main__':
    import os
    total = 0
    for dirn, dirns, filens in os.walk('.'):
        for f in filens:
            if f.endswith('.py'):
                delt = len(open(f'{dirn}/{f}').readlines())
                print(f'文件{dirn}/{f}，有码{delt}行')
                total += delt

    print(f'统计完毕，在本文件夹{os.path.dirname(__file__)}中共有代码{total}行')