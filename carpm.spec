Name:		carpm
Summary:	Script to help rpm's managing in command-line
Version:	2.2
Release:	5
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3
Group:		System/Configuration/Packaging
URL:		https://carpm.sourceforge.net
BuildRequires:	bash
Requires:	rpm
Requires:	urpmi  
Requires:	bash
BuildArch:  noarch

%description
Carpm is a script, a text tool for help you to managing your rpm and your rpm
database.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %name %{buildroot}/%{_bindir}


%files
%doc INSTALL COPYING
%{_bindir}/%{name}


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-3mdv2011.0
+ Revision: 610096
- rebuild

* Sun Apr 25 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.2-2mdv2010.1
+ Revision: 538632
- don't define name version release on top of spec.
- use the tar.bz2 given by upstream
- package doc

* Thu Feb 25 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.2-1mdv2010.1
+ Revision: 511170
- up to 2.2

* Wed Feb 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.1-2mdv2010.1
+ Revision: 510583
- fix rel
- fix version

* Wed Feb 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.1-1mdv2010.1
+ Revision: 510578
- new version 2.1

* Sat Feb 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.0-1mdv2010.1
+ Revision: 508732
- import carpm


