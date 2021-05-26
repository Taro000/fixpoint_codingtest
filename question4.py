import sys 
import datetime

def main(logfile, N):
    with open(logfile) as f:
        log_list = [r.strip().split(',') for r in f.readlines()]
        each_subnet_logs = {}
        for log in log_list:
            network_len = int(log[1].split('/')[1]) / 8
            network_area = ','.join(log[1].split('.')[:int(network_len)])
            each_subnet_logs[network_area] = []
            for log2 in log_list:
                if network_area == ','.join(log2[1].split('.')[:int(network_len)]):
                    each_subnet_logs[network_area].append(log2)
        
        for logs in each_subnet_logs.values():
            timeout_count = 0
            for i in range(len(logs)):
                if logs[i][-1] == '-':
                    timeout_count += 1
                    if timeout_count >= int(N):
                        if i != len(logs)-1:
                            error_time = datetime.datetime.strptime(logs[i+1][0], '%Y%m%d%H%M%S') - datetime.datetime.strptime(logs[i][0], '%Y%m%d%H%M%S')
                            print(logs[i][1], error_time)
                            if logs[i+1][-1] != '-':
                                timeout_count = 0
                        else:
                            print(logs[i][1], '-')



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])