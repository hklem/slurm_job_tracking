.. |running_example| image:: https://github.com/hklem/slurm_job_tracking/jobcheck.png

Slurm Job Tracking
------------------

A Python script that will allow you to track completion of slurm jobs. Especially useful if you are running numerous jobs in numerous locations. 

To install and use:

* Copy jobcheck.py to machine
    - https://github.com/hklem/slurm_job_tracking/jobcheck.py
    - You can copy the file anywhere; I chose my home directory.
    
* (optional) Add alias to your .bashrc >> alias sq 'python ~/jobcheck.py'
* Run command
    - When you run for the first time, the script initializes and logs current job information. Thereafter it will work like normal:    
.. centered:: |running_example|
