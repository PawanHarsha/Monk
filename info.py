from msvcrt import kbhit
import jenkins
from beautifultable import BeautifulTable 
table= BeautifulTable()
class buildjobs:
    global k
    k=0
    def info():
        jobs_count=server.jobs_count()
        print("Total number of jobs present are:", jobs_count)
        s=input("do you wish to print all the jobs,Y/N: ")
        A=[]
        for i in range(jobs_count):
            if server.get_all_jobs()[i].get("_class") == "org.jenkinsci.plugins.workflow.job.WorkflowJob":
                A.append(server.get_all_jobs()[i].get("name"))
        
        def choice_(k):
            if k==1:
                jobname_=input("Type the job name for more information(press 'enter' if not): ")
                if bool(jobname_)== True:
                    if server.job_exists(jobname_) == True:
                        print(server.get_job_info(jobname_))
                    else: 
                        print("Job doesn't exist")
                p=input("do you wish to see complete build information of all the jobs,Y/N: ")
                builds_(p)
            if k==2:
                jobinfo=['name', 'description', 'buildable', 'color', 'firstBuild', 'healthReport', 'inQueue', 'lastBuild', 'lastCompletedBuild', 'lastFailedBuild', 'lastStableBuild', 'lastSuccessfulBuild', 'lastUnstableBuild', 'lastUnsuccessfulBuild', 'nextBuildNumber',  'queueItem', 'concurrentBuild', 'disabled', 'downstreamProjects', 'labelExpression', 'scm', 'upstreamProjects']
                table.columns.header = jobinfo
                table.rows.header = A
                for j in range(len(A)):
                    for l in range(len(jobinfo)):
                        B= server.get_job_info(A[j])

        def builds_(p):
            global k
            if p=="Y":
                if k==0:
                    print(A) 
                k+=1
                choice_(k)
                
            if p=="N":
                k+=1
                choice_(k)
            else:
                print("wrong input")
                p=input("Y/N?: ")
                builds_(p)
        builds_(s)
    
    def info_b():
    def info_q():

        
class plugins():
    def info():


username_=input("enter the login username: ")
passwd_=input("enter password: ")
#host_name=
#port=
server = jenkins.Jenkins('http://localhost:8080', username= username_ , password= passwd_)
print("Welcome to the jenkins monitoring tool")
items=input("please select an option: 1.Jobs 2.plugin information 3.node status 4.userinformation: ")

if items=="1": 
    print (buildjobs.info())
"""elif items=="2":
    plugins()
elif items=="3":
    nodes()
elif items=="4":
    viewuser()
else: print("wrong choice")


def create_newjob():
    def build_info():
    




        server.get_job_info()
        server.get_job_info_regex()
        server.get_job_name(name)
        
        get_running_builds()
        get_build_env_vars(name, number, depth=0)
        get_build_test_report(name, number, depth=0)
        get_queue_info()
        cancel_queue(id)
        server.get_all_jobs()
        
        
        set_next_build_number(name, number)
        copy_job(from_name, to_name)
        rename_job(from_name, to_name)
        delete_job(name)
        enable_job(name)
        disable_job(name)
        assert_job_exists(name, exception_message='job[%s] does not exist')
        create_job(name, config_xml)
        get_job_config(name)
        reconfig_job(name, config_xml)
        build_job_url(name, parameters=None, token=None)
        build_job(name, parameters=None, token=None)
        stop_build(name, number)
        delete_build(name, number)
        wipeout_job_workspace(name)



class Plugins:
class viewuser:
class nodes:

#check whether a plugin is present
#node specification"""
