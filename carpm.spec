Name:		carpm
Summary:	Script to help rpm's managing in command-line
Version:	2.2
Release:	%mkrel 3
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3
Group:		System/Configuration/Packaging
URL:		http://carpm.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	bash
Requires:	rpm
Requires:	urpmi  
Requires:	bash

%description
Carpm is a script, a text tool for help you to managing your rpm and your rpm database.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 %name %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL COPYING
%{_bindir}/%{name}
