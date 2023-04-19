import os

### === INITIALIZE === ###

script_name = os.path.realpath(__file__).split('/')[-1]
wdir = os.path.realpath(__file__).split(script_name)[0]
os.chdir(wdir)

### === FUNCTIONS === ###
print_q = 'squeue --user=`whoami` --format="%.7A %.35j %.10u %.7C %.10M %.15l %.20R"'
def store_job_info():
    os.system(print_q + ' > current_queue.tmp')
    file = open('current_queue.tmp','r')
    lines = file.readlines()
    file.close()
    job_names = []
    job_ids = []
    working_dirs = []
    for line in lines[1:]:
        job_name = line.split()[1]
        job_id = line.split()[0]
        os.system('scontrol show job {} > jobinfo.tmp'.format(job_id))
        file2 = open('jobinfo.tmp','r')
        lines2 = file2.readlines()
        file2.close()
        for line2 in lines2:
            if 'WorkDir' in line2:
                working_dir = line2.split('WorkDir=')[1].split('\n')[0]
        job_names.append(job_name)
        job_ids.append(job_id)
        working_dirs.append(working_dir)
    os.system('rm current_queue.tmp')
    os.system('rm jobinfo.tmp') 
    with open('.current_jobs.txt','w') as f:
        for job in range(len(job_ids)):
            f.write(job_ids[job])
            f.write('\t')
            f.write(job_names[job])
            f.write('\t')
            f.write(working_dirs[job])
            f.write('\n')
    return job_ids

def find_completed_jobs(job_ids):
    file = open('.previous_jobs.txt','r')
    lines = file.readlines()
    file.close()
    count = 0
    for line in lines:
        if line.split()[0] not in job_ids:
            count += 1
            print('This job is no longer running since the last time you checked: \n NAME: {} \n JOB ID: {} \n Working Directory: {}.'.format(line.split()[1],line.split()[0],line.split()[2]))
    if count == 0:
        print('No jobs have ended since the last time you checked!')


### === MAIN === ###
if '.current_jobs.txt' not in os.listdir():
    print('No previously submitted jobs are stored. Either the file was deleted or this is your first time running this script.')
    store_job_info()
    print('The current running jobs have now been stored. Run this script again and you should not see this message.')

else:
    os.system('mv .current_jobs.txt .previous_jobs.txt')
    job_ids = store_job_info()
    print('Jobs you are currently running:')
    print('================================================================================================================')
    os.system(print_q)
    print('================================================================================================================')
    find_completed_jobs(job_ids)
    print('================================================================================================================')

