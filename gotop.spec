%global goipath github.com/cjbassi/gotop
%global commit 867cf2b9e4a4acfd8bbfbe5c8d67aa2450d669e2
%gometa -i

Name:     gotop
Version:  3.0.0
Release:  1

Summary:  A terminal based graphical activity monitor inspired by gtop and vtop
License:  AGPL-3.0
Group:    Other
Url:      https://github.com/cjbassi/gotop
Source0:  https://github.com/cjbassi/gotop/archive/%{version}.tar.gz

BuildRequires: golang

%description
%summary

%prep
%setup -n %{name}-%{version}

%build
%gobuild

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%_bindir/%{name}
