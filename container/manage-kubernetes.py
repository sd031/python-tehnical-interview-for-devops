#pip install kubernetes

from kubernetes import client, config

# Configure API access
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
pods = v1.list_namespaced_pod(namespace="default")

for pod in pods.items:
    print(f"{pod.metadata.name}\t{pod.status.pod_ip}")
