# Docker Swarm Vagrant Ansible

This is a simple deployment of a high available application.

## Docker Swarm
Docker Swarm is a Docker clustering solution, it turns multiple physical (or virtual) hosts into a one cluster, which practically behaves as a single Docker host. Swarm additionally gives you tools and mechiasms to easily scale your containers and create managed services with automatic load balancing to the exposed ports.

Swarm uses [Raft Consensus Algortihm](http://thesecretlivesofdata.com/raft/) to manage the cluster state. Swarm can tolerate `(N-1)/2` failures and needs `(N/2)+1` nodes to agree on values.

## Dependencies
* Ansible
* Vagrant

## Deployment
```bash
ansible-playbook -i inventory deploy.yml
```

## Destroy(ment)
```bash
vagrant destroy -f
```

## Behaviour
The cluster provides an API call to http://<IP>/app
When a POST request is sent to that API method, the application will store the timestamp into a database.

## Usage
```bash
curl -X POST http://192.168.10.2/app
```
Expected output:
```json
{
  "epoch": 1510659852.600444,
  "hostname": "ca425c25b7a9",
  "records": 3,
  "status": "saved",
  "timestamp": "2017-11-14 11:44:12"
}
```

## Docker container
The container that is deployed in the workers is build with the files that are in the folder ```container``` and published to http://cloud.docker.com/ from where is picked by the swarm to run it on the workers.

## Technologies
* Ansible
* Vagrant
* VirtualBox
* Ubuntu
* Docker
* Flask
* Python
* Redis

## Customization
By default, 3 machines are created: `manager`, `worker1`, `worker2`. You can adjust how many
workers you want in the `Vagrantfile`, by setting the `numworkers` variable. Manager, by default, has address "192.168.10.2", workers have consecutive IPs.

```ruby
numworkers = 2
```

If your provisioner is `VirtualBox`, you can modify the vm allocations for memory and cpu by changing these variables:

```ruby
vmmemory = 512
```

```ruby
numcpu = 1
```

# License
MIT

# Author
Sergiu Marsavela @marsavela
