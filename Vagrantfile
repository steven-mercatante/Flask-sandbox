# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  config.vm.box = "hashicorp/precise32"

  config.vm.network :forwarded_port, host: 8080, guest: 80

  # It's standard practice for Flask apps to run on port 5000 during development
  config.vm.network :forwarded_port, host: 5050, guest: 5000

  config.vm.network :forwarded_port, host: 2220, guest: 22

  # Installs required server software
  config.vm.provision :ansible do |ansible|
    ansible.sudo = true
    ansible.verbose = "vvvv"
    ansible.playbook = "provisioning/install-requirements.yml"
  end

  # Creates a python virtual environment and installs the specified python
  # packages
  config.vm.provision :shell, path: "provisioning/setup-python-venv.sh"

end
