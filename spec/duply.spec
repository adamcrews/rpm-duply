%global VERSION 1.10.1
%global Release 1

Name:           duply
Version:        %{VERSION}
Release:        %{Release}%{?dist}
Summary:        Wrapper for duplicity
Group:          Applications/Archiving
License:        GPLv2
URL:            http://duply.net/
Source0:        http://downloads.sourceforge.net/ftplicity/%{name}_%{VERSION}.tgz
#BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  txt2man >= 1.5.6
Requires:       duplicity


%description
duply deals as a wrapper for the mighty duplicity magic. It simplifies
running duplicity with cron or on command line by:

- keeping recurring settings in profiles per backup job
- enabling batch operations e.g. backup_verify_purge
- executing pre/post scripts
- precondition checking for flawless duplicity operation

Since version 1.5.0 all duplicity backends are supported. Hence the
name changed from ftplicity to duply.


%prep
%setup -q -n %{name}_%{VERSION}
iconv -f iso-8859-1 -t utf-8 %{name} > %{name}.tmp
mv %{name}{.tmp,}


%build
# generate the man page
chmod +x %{name}
./%{name} txt2man > %{name}.1


%install
rm -rf %{buildroot}
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
# root's profiles will be stored there
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
# fix shebang line
sed -i "1c#!/bin/bash" %{buildroot}%{_bindir}/%{name}
mv gpl-2.0.txt LICENSE


%clean
rm -rf %{buildroot}


%files
%doc LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_sysconfdir}/%{name}


%changelog
* Thu Sep 03 2015 Adam Crews <adam.crews@gmail.com> - 1.10.1-1
- Update to 1.10.1

* Tue Jan 28 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.6.0-1
- Update to 1.6.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.11-1
- Update to 1.5.11.

* Thu Apr  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.10-1
- Update to 1.5.10.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.9-1
- Update to 1.5.9.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.7-1
- Update to 1.5.7.

* Tue Jun  5 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.6-1
- Updte to 1.5.6.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5.5-1
- Update to 1.5.5.5.

* Fri Nov 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5.4-1
- Update to 1.5.5.4.
- Rename license file to LICENSE.
- Remove %%defattr directive in %%files.

* Tue Jul  5 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5.1-1
- Update to 1.5.5.1.

* Tue May 10 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.5-1
- Update to 1.5.5.
- Generate and pack a man page.

* Wed Feb 23 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.4.2-2
- Convert duply script to UTF-8.

* Thu Feb  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.4.2-1
- New package.
