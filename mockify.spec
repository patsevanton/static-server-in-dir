Name:           mockify
Version:        0.1
Release:        3
Summary:        Easy, configurable API mocking you can change on-the-fly
License:        ASL 2.0 
Source0:        mockify.service
Source1:        routes.yaml
BuildRequires:  golang
BuildRequires:  tree
Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/echo, /usr/bin/chown
Requires(postun): /usr/sbin/userdel

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)

%if %use_systemd
BuildRequires: systemd
%endif

%description
Easy, configurable API mocking you can change on-the-fly

%build
export GOPATH=%{_builddir}/_build
go get github.com/gorilla/mux
go get github.com/json-iterator/go
go get github.com/sirupsen/logrus
go get gopkg.in/yaml.v2
mkdir -p $GOPATH/src/github.com/patsevanton
git clone https://github.com/patsevanton/mockify.git $GOPATH/src/github.com/patsevanton/mockify
go build -o mockify $GOPATH/src/github.com/patsevanton/mockify/app/cmd/mockify.go

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 mockify %{buildroot}%{_bindir}/mockify
install -d %{buildroot}/etc/mockify
ls
pwd
cp %{SOURCE1} %{buildroot}/etc/mockify/routes.yaml
%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} \
    %{buildroot}%{_unitdir}/mockify.service
%endif

%pre
/usr/bin/getent group mockify > /dev/null || /usr/sbin/groupadd -r mockify
/usr/bin/getent passwd mockify > /dev/null || /usr/sbin/useradd -r -d /usr/lib/mockify -s /bin/bash -g mockify mockify

%post
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%preun
%if %use_systemd
/usr/bin/systemctl stop mockify
%endif

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%files
%defattr(-,mockify,mockify,-)
%{_bindir}/mockify
/etc/mockify/routes.yaml
%if %{use_systemd}
%{_unitdir}/mockify.service
%endif
