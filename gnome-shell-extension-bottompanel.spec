%define mintname mgse-bottompanel

Name:           gnome-shell-extension-bottompanel
Version:        1.0.3
Release:        1%{?dist}.R
Summary:        Bottom panel for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv3
URL:            http://www.linuxmint.com
Source0:        http://ppa.launchpad.net/ikoinoba/ppa/ubuntu/pool/main/m/%{mintname}/%{mintname}_%{version}-0~ppa4.tar.gz
BuildArch:      noarch
Requires:       gnome-shell >= 3.2

%description 
%{name} is a simple Gnome shell
extension that adds bottom panel as in GNOME 2.

%prep
%setup -q -n %{mintname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/
cp -r ./usr/share/gnome-shell/extensions/* $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/

%files
%defattr(-,root,root,-)
%{_datadir}/gnome-shell/extensions/*
%doc TODO

%changelog
* Mon Nov 27 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 1.0.3-1.R
- initial build for Fedora
