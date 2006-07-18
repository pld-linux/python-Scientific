#
# TODO:
# 1. tkwidgets to separate package
#


%define 	pname	Scientific
%define		mname	%{pname}Python

Summary:	Various Python modules for scientific computing
Summary(pl):	Ró¿ne modu³y Pythona dla obliczeñ naukowych
Name:		python-%{pname}
Version:	2.4.9
Release:	1
Group:		Libraries/Python
License:	LGPL
Source0:	http://starship.python.net/~hinsen/ScientificPython/%{mname}-%{version}.tar.gz
# Source0-md5:	a88602846bdb8a1e2c9f21dc3cf81341
URL:		http://starship.python.net/crew/hinsen/scientific.html
BuildRequires:	netcdf-devel
BuildRequires:	python-Numeric-devel
BuildRequires:	python-tkinter
Requires:	python-Numeric
Requires:	python-tkinter
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various Python modules for scientific computing.

%description -l pl
Ró¿ne modu³y Pythona dla obliczeñ naukowych.

%prep
%setup -q -n %{mname}-%{version}

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT --optimize=2

#Removing *.py files
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.py"|xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.MPI Doc/HTML Doc/PDF
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/%{pname}
%{py_sitedir}/%{pname}/*.py[co]
%{py_sitedir}/%{pname}/BSP
%{py_sitedir}/%{pname}/Functions
%{py_sitedir}/%{pname}/Geometry
%{py_sitedir}/%{pname}/IO
%{py_sitedir}/%{pname}/MPI
%{py_sitedir}/%{pname}/Physics
%{py_sitedir}/%{pname}/Signals
%{py_sitedir}/%{pname}/Statistics
%{py_sitedir}/%{pname}/Threading
%{py_sitedir}/%{pname}/TkWidgets
%{py_sitedir}/%{pname}/Visualization
%dir %{py_sitedir}/%{pname}/linux2
%attr(755,root,root) %{py_sitedir}/%{pname}/linux2/Scientific_netcdf.so
%{py_incdir}/%{pname}
