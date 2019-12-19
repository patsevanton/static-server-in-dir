%global _prefix /usr/local

Name:           static-server-in-dir
Version:        0.4
Release:        1
Summary:        Http static server in your current (or specified) directory
License:        ASL 2.0 
Source0:        main.go
BuildRequires:  golang

%description
A simple Golang http static server in your current (or specified) directory.

%build
export GOPATH=%{_builddir}/_build
go get github.com/AlexanderGrom/go-starter
mkdir -p $GOPATH/src/github.com/patsevanton
git clone https://github.com/patsevanton/static-server-in-dir.git $GOPATH/src/github.com/patsevanton/static-server-in-dir
go build -o static-server-in-dir $GOPATH/src/github.com/patsevanton/static-server-in-dir/main.go

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./static-server-in-dir %{buildroot}%{_bindir}/static-server-in-dir

%files
%defattr(-,root,root,-)
%{_bindir}/static-server-in-dir
