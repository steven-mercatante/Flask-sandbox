Vagrant:
--------
- Initialize database by feeding Ansible the `.env` variables
- Install PostgreSQL

Python:
-------
- Include Redis 
- Enable config based toggle of requiring Users to be confirmed before they can
log in. This would affect sending registration confirmation emails and checking
confirmed status during login.
- Enable config based setting of logging user in based on email and/or username
- Bootstrap script to create initial `.env` file and populate with random secret key
- Abstract User model logic into UserService class