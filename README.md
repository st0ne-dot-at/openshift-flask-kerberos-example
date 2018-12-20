# OpenShift 3 Flask Kerberos Example

## Quick Start
1. clone repository

    git clone https://github.com/st0ne-dot-at/openshift-flask-kerberos-example.git

2. create  and configure python_ansbile27 virtualenv

    virtualenv -p /usr/bin/python2 python_ansible27
    . python_ansible27/bin/activate
    pip install -r ansible_requirements.txt

3. adapt hosts to your needs

    [hosts](hosts)

4. depoy application

    ansible-playbook -i hosts ansible/playbooks/deploy_app.yml \
         --extra-vars="ansible_python_interpreter=$(which python)"

5. kinit

    kinit myuser@MYDOMAIN.ORG

6. test kerberos with curl

    curl -u : --negotiate https://myservice.osc.mydomain.org -v

## Cleanup

1. remove app `oc delete all --selector template=flask-krb5-auth-sample
