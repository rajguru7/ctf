## Osiris hack night

Context: 
<https://youtu.be/NV9dx4YhvKc?si=Wd6EGHLf3KQRHApe>


### BugBounty

Portswigger web academy - go through all of it.

Use Burpsuite, nmap, sqlmap 
Evil Nginx - phishing, can catch MFA tokens

SAML raider extension 

In case you need a public ip to catch a reverse shell. 10 USD/month on digital
ocean for public linux server. This is helpful.
Helpful to have short domain - in case there is a limit on the amount of text
you have to enter into a text field.

You can choose Desktop, mobile, web, AI/LLM - you can get money if you are able
to generate a biased response using a prompt.

Manual hunters - holistic assessment
Automation hunters - does work out for some people (They are very experienced,
around 10 years but they pay a lot (thousands of dollars) in cloud computing)

Pick a platform - Bugcrowd
VDP platform - no payout, good for learning.
<https://bugcrowd.com/engagements?category=vdp&sort_by=promoted&sort_direction=desc&page=1>
Read hackerone disclosed reports to find out what 

It'll be tough to find a bug, wake up every single morning. Try to stick to a
program for at least 8 hours before switching to another program.

Common issues you can find:
PDF generators are tough to implement - so there could be a bug there
LFI was found. The HTML renders a local file in iframe.
Access control type issues
IDOR issue

### Pen testing

Certifications - very important
Resume Fodder - make a site and write about what ctfs you participated in and
what bug bounties you worked on (blogging), publish CVEs, keep good github
profile.
Networking - Connections through discord, defcon
Prior Work Experience - bug bounty successful submissions can be considered as
work experience.
Soft Skills 
Internal vs. Consulting Positions - when applying to jobs consider this aspect
consulting - different applications many times.


### Infrastructure Security

#### Docker

CSAW costs 5k USD for 3 days - Hosting is expensive

containers are processes with isolation and resource management
namespace - limit what you can see
cgroups - limit what you can use


* You can control resources used by a container using cgroups.
* So use --pids-limit 10 option when running the docker container to limit the
  number of processes that can be run in the container. So a fork bomb run
  inside the container will stop after 10 processes are created.
* This provides security.

#### Kubernetes

* etcd - stores the cluster management state
* kubelet - runs on every node, manages containers

##### Security in Kubernetes

* Namespacing
* RBAC
* Network Policies
* Service Accounts


#### Anubis

Features:

* Cloud IDEs
* Autograding
* Runs on Digital Ocean
* Each IDE instance uses multiple containers to run
    * One container for the IDE
    * One container for setting up the environment
    * One container for running docker commands separately
* It is better to give the response fast and assign the work behind the scenes
  in distributed computing.
* Traefik Ingress has multiple proxy routers behind which decides which request
  goes to which IDE based on the cookie.
* Proxy Routers
    * Read the cookie, get data from database and then decide which IDE to route
      to.

Vulnerability in proxy router
* ip address cached in proxy router. If IDE is removed, the ip address is not
  removed from the cache. So if a new IDE is created with the same ip address
  then the request will be routed to the old IDE.
* Happened during a final exam.
 

