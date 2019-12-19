%global _prefix /usr/local

Name:    static-server-in-dir
Version: 0.2
Release: 1
Summary: Http static server in your current (or specified) directory
Group:   Development Tools
License: ASL 2.0
Source0: static-server-in-dir.service
Requires: ruby

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)

%description
Http static server in your current (or specified) directory

%install
%if %{use_systemd}
%{__install} -m 0755 -d %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} \
    %{buildroot}%{_unitdir}/%{name}.service
%endif
pwd
ls
ls %{_unitdir}

%post
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%preun
%if %use_systemd
/usr/bin/systemctl stop %{name}
%endif

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%files
%if %{use_systemd}
%{_unitdir}/%{name}.service
%endif
