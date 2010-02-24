%define	name	carpm
%define	version	2.1
%define	release	%mkrel	2

Name:		%{name}
Summary:	Script to help rpm's managing in command-line
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}
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

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 %SOURCE0 %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}-%{version}
