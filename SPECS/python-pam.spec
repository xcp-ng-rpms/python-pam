%global package_speccommit 5ade927d5590dc722cba842c173737a6eefc8a9e
%global usver 1.8.4
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
Name:           python-pam
Version:        1.8.4
Release:        %{?xsrel}%{?dist}
Summary:        Pure Python interface to the Pluggable Authentication Modules system on Linux
License:        MIT
URL:            https://github.com/FirefighterBlu3/python-pam
Source0: python-pam-1.8.4.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This module provides an authenticate function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

%package -n python3-pam
Summary:        Pure Python interface to the Pluggable Authentication Modules system on Linux
%{?python_provide:%python_provide python3-pam}

%description -n python3-pam
This module provides an authenticate function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files -n python3-pam
%doc README.md
%license LICENSE
%{python3_sitelib}/pam.py*
%{python3_sitelib}/python_pam*-%{version}-py*.egg-info
%{python3_sitelib}/__pycache__/pam.cpython*

%changelog
* Thu Nov 9 2023 Qin Zhang <qin.zhang@citrix.com> - 1.8.4-1
- First imported release

