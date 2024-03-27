Role Name
=========

ansible-thingsboard deploys thingsboard using docker.

Requirements
------------

docker

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - name: Deploy ThingsBoard
      hosts: localhost
      become: yes 
      roles:
        - ansible-thingsboard

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

Refs: https://thingsboard.io/docs/user-guide/install/docker/
