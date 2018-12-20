# OpenShift 3 Flask Kerberos Example
This repo provides an kerberized flask app and ansible playbooks to deploy the app on an OpenShift v3 cluster.

## Prerequisites
1. OpenShift v3 Cluster
2. ActiveDirectory admin user (configured in [hosts](hosts) ... bind_dn)
3. ActiveDirectory service user. (configured in [hosts](hosts) ... mapped_user). The servicePrincipal get mapped on that user via the ansibe ldap_attr module.

## Quick Start
1. clone repository
```
git clone https://github.com/st0ne-dot-at/openshift-flask-kerberos-example.git
```

2. create  and configure python_ansbile27 virtualenv

```
virtualenv -p /usr/bin/python2 python_ansible27
. python_ansible27/bin/activate
pip install -r ansible_requirements.txt
```

3. adapt hosts to your needs

    [hosts](hosts)

4. depoy application

```
ansible-playbook -i hosts ansible/playbooks/deploy_app.yml \
         --extra-vars="ansible_python_interpreter=$(which python)"
```

5. kinit

```
kinit myuser@MYDOMAIN.ORG
```
6. test kerberos with curl

```
curl -u : --negotiate https://myservice.osc.mydomain.org -v
```

## Cleanup

1. remove app
```
oc delete all --selector template=flask-krb5-auth-sample
```

## Rebuild

```
oc start-build flask-krb5-app
```

