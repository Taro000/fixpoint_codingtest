import sys 
import datetime

def main(logfile):
    with open(logfile) as f:
        log_list = [r.strip().split(',') for r in f.readlines()]
        for i in range(len(log_list)):
            if log_list[i][-1] == '-':
                if i != len(log_list)-1:
                    error_time = datetime.datetime.strptime(log_list[i+1][0], '%Y%m%d%H%M%S') - datetime.datetime.strptime(log_list[i][0], '%Y%m%d%H%M%S')
                    print(log_list[i][1], error_time.total_seconds())
                else:
                    print(log_list[i][1], '-')


if __name__ == '__main__':
    main(sys.argv[1])