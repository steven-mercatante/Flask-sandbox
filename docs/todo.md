Vagrant:
--------
- Install Redis
- Initialize database by feeding Ansible the `.env` variables
- Install PostgreSQL

Python:
-------
- Include Redis 
- Enable config based toggle of auth registration
- Enable config based toggle of checking if user is confirmed during login
- Bootstrap script to create initial `.env` file and populate with random secret key