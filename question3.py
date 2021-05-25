import sys 
import datetime

def main(logfile, N, m, t):
    with open(logfile) as f:
        log_list = [r.strip().split(',') for r in f.readlines()]
        eatch_server_logs = {}
        for log in log_list:
            eatch_server_logs[log[1]] = []
            for log2 in log_list:
                if log[1] == log2[1]:
                    eatch_server_logs[log[1]].append(log2)
        
        for logs in eatch_server_logs.values():
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
                elif i >= int(m)-1:
                    last_m_sum = sum([int(l[-1]) for l in logs[i+1-int(m):i+1] if l[-1] != '-'])
                    return_time_avg = last_m_sum / (int(m))
                    if return_time_avg > int(t):
                        print(logs[i][1], return_time_avg)



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])