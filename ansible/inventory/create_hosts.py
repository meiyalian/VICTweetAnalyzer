def read_hosts(host_number):
    with open("inventory/hosts.ini") as f: 
        has_hosts=False
        hosts=[]
        for line in f.readlines():
            line = line.replace("\n","")
            if len(hosts)==host_number:
                has_hosts=False
            if has_hosts: 
                hosts.append(line)
            if line == "[instances]":
                has_hosts = True
           
        with open ("inventory/host_job.ini","w") as file:
            print(hosts)
            file.write("[instances]\n")
            for host in hosts:
                print(host)
                file.write(host)
                file.write("\n")
            file.write("\n")
    return hosts
def create_jobs_couchdb(hosts,masternode,workers=[]):
    # with open("inventory/hosts.ini") as f: 
    #     has_hosts=False
    #     hosts=[]
    #     for line in f.readlines():
    #         line = line.replace("\n","")
    with open("inventory/host_job.ini", "a") as file:
            file.write("[database:children]\n")
            file.write("masternode\n")
            file.write("workers\n")
            file.write("\n")
            file.write("[masternode]\n")
            file.write("{}".format(hosts[masternode]))
            file.write("\n\n")
            file.write("[workers]\n")
            file.write("{}".format(hosts[workers[0]]))
            file.write("\n")
            file.write("{}".format(hosts[workers[1]]))
            file.write("\n")
            file.write("\n")

def create_jobs_crawler_stream(hosts,worker):
    with open("inventory/host_job.ini", "a") as file:
            file.write("[crawler-stream]\n")
            file.write("{}".format(hosts[worker]))
            file.write("\n")
            file.write("\n")
def create_jobs_crawler_search(hosts,worker):
    with open("inventory/host_job.ini", "a") as file:
            file.write("[crawler-search]\n")
            file.write("{}".format(hosts[worker]))
            file.write("\n")
            file.write("\n")
def create_jobs_backend(hosts,worker):
    with open("inventory/host_job.ini", "a") as file:
            file.write("[backend]\n")
            file.write("{}".format(hosts[worker]))
            file.write("\n")
            file.write("\n")
def create_jobs_frontend(hosts,worker):
    with open("inventory/host_job.ini", "a") as file:
            file.write("[frontend]\n")
            file.write("{}".format(hosts[worker]))
            file.write("\n")  
            file.write("\n")      
def create_jobs_analysis(hosts,worker):
    with open("inventory/host_job.ini", "a") as file:
            file.write("[analysis]\n")
            file.write("{}".format(hosts[worker]))
            file.write("\n")  
            file.write("\n")        
if __name__ == "__main__":
    hosts=read_hosts(4)
    create_jobs_couchdb(hosts,1,[2,3])
    create_jobs_crawler_stream(hosts,1)
    create_jobs_crawler_search(hosts,2)
    create_jobs_backend(hosts,0)
    create_jobs_frontend(hosts,2)
    create_jobs_analysis(hosts,3)
