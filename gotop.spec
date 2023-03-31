%global goipath github.com/xxxserxxx/gotop
%define  _empty_manifest_terminate_build 0

Name:     gotop
Version:  4.1.3
Release:  2

Summary:  A terminal based graphical activity monitor inspired by gtop and vtop
License:  AGPL-3.0
Group:    Other
Url:      https://github.com/xxxserxxx/gotop
Source0:  https://github.com/xxxserxxx/gotop/archive/%{name}-%{version}.tar.gz

BuildRequires: golang

%description
%summary

%prep
%autosetup -n %{name}-%{version}

%build
go build -o gotop \
        -ldflags "-X main.Version=v${VERS} -X main.BuildDate=${DAT}" \
        ./cmd/gotop

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%_bindir/%{name}
