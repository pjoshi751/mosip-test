
The hardware compute and storage requirements for MOSIP core platform are estimated as below.

## Compute 

|Module|Capacity|N Servers|Configuration|
|---|---|---|---|
Pre-registration | 300 concurrent users | 20 | 4 CPU, 16 GB RAM |
Registration Processor | 200,000 registrations per day | 80 | 4 CPU, 16 GB RAM|
ID Authentication | 2,000,000 auth requests per day | 20 | 4 CPU, 16 GB RAM |

We estimate 30% additional compute capacitiy for administration, monitoring and maintenance.

**Notes** 
1. The above figures are estimates, derived from performance testing on sandbox setup.
1. High availability is taken into consideration with assumed replication factor of 2 per service pod/docker 
1. The above estimates **do not** include compute servers needed for
   1. Database
   1. HDFS/CEPH
   1. Bio SDK:  compute requirements should be provided by the SDK vendor.
   1. HSM 
   1. ABIS
   1. Virus scan
   1. Load balancers
   1. External IAM
   1. Disaster recovery:  Setup will be replicated, hence, double the number of servers.

## Storage
Storage requirement estimates.

## All hardware components 
This section lists the various hardware components needed for deploying MOSIP platform. 
1. Compute machines (VM/Bare Metal)
1. DB machines
1. Storage SAN/NAS 
1. HSM (Hardware Security Module)
1. Load Balancers
1. Firewalls
1. Routers/Software Defined Network
1. IDS/IPS
1. Laptops with TPM (for registrations)
1. Fingerprint slap scanners
1. Iris scanners
1. Camera
1. Document scanners (optional)
1. Printers (optional)




