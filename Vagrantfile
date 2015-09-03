# -*- mode: ruby -*-
# vi: set ft=ruby :

# This Vagrantfile will build an RPM of the current version of the RPM spec
# Just run vagrant up, and wait for the rpm and srpm to be written to the cwd.

$buildrpm = <<BUILDRPM
echo "Running the build script"

VERSION=`awk '/^%global VERSION/{print $NF}' /vagrant/spec/duply.spec`
RELEASE=`awk '/^%global Release/{print $NF}' /vagrant/spec/duply.spec`
NAME=`awk '/^Name:/{print $NF}' /vagrant/spec/duply.spec`
BUILD_REQUIRES=`awk -F: '/^BuildRequires/ {req_line=$2 ; split(req_line,dep_array,","); for (item in dep_array) { split(dep_array[item],final_deps," "); for (dependancy in final_deps) printf "%s ", final_deps[1]}}' /vagrant/spec/duply.spec`
TMPSOURCE=`awk '/^Source0:/{print $NF}' /vagrant/spec/duply.spec`
SOURCE=`echo ${TMPSOURCE} | sed -e "s/%{name}/$NAME/g" -e "s/%{VERSION}/$VERSION/g"`

echo "VERSION: ${VERSION}"
echo "RELEASE: ${RELEASE}"
echo "BUILD_REQUIRES: ${BUILD_REQUIRES}"

echo "Building ${NAME} ${VERSION}"
echo "Installing dependencies via yum"

sudo yum install -y epel-release
sudo yum clean metadata
sudo yum groupinstall -y 'Development tools'
sudo yum install -y rpmdevtools ${BUILD_REQUIRES}
echo "Dependencies installed."

echo "Setting up RPM build env"
rpmdev-setuptree

echo "Getting Source"
curl -v -L -o ~/rpmbuild/SOURCES/${NAME}_${VERSION}.tgz "${SOURCE}"

echo "Copying source and config to rpm env"
cp /vagrant/spec/*.spec ~/rpmbuild/SPECS/

echo "Building..."
cd ~/rpmbuild/
rpmbuild -ba SPECS/${NAME}.spec

echo "Copying output to the vagrant share."
cp ~/rpmbuild/RPMS/*/* /vagrant
cp ~/rpmbuild/SRPMS/* /vagrant

echo "Done building ${NAME} ${VERSION}-${RELEASE}"
BUILDRPM

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Bare bones CentOS 6.5 box from a trustworthy community member.
  config.vm.box = "puppetlabs/centos-6.6-64-nocm"

  # This optional plugin caches RPMs for faster rebuilds.
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :machine
  end

  config.vm.provision "shell", privileged: false, inline: $buildrpm
end
