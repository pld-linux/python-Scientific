#
# TODO:
# 1. tkwidgets to separate package
#

%include	/usr/lib/rpm/macros.python

%define 	pname	Scientific
%define		mname	%{pname}Python

Summary:	Various Python modules for scientific computing
Summary(pl):	Ró¿ne modu³y Pythona dla obliczeñ naukowych
Name:		python-%{pname}
Version:	2.2
Release:	3
Group:		Libraries/Python
License:	LGPL
Source0:	http://starship.python.net/crew/hinsen/%{mname}-%{version}.tar.gz
# Source0-md5:	c5c5ecfe6d6973d5c8d465ccf192b266
URL:		http://starship.python.net/crew/hinsen/scientific.html
BuildRequires:	netcdf-devel
BuildRequires:	python-numpy-devel
BuildRequires:	python-tkinter
Requires:	python-numpy
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
CC=%{__cc}; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.MPI Doc/HTML Doc/PDF
%dir %{py_sitedir}/%{pname}
%dir %{py_sitedir}/%{pname}/Functions
%dir %{py_sitedir}/%{pname}/Geometry
%dir %{py_sitedir}/%{pname}/IO
%dir %{py_sitedir}/%{pname}/MPI
%dir %{py_sitedir}/%{pname}/Physics
%dir %{py_sitedir}/%{pname}/Statistics
%dir %{py_sitedir}/%{pname}/Threading
%dir %{py_sitedir}/%{pname}/TkWidgets
%dir %{py_sitedir}/%{pname}/Visualization
%{py_sitedir}/%{pname}/Functions/*.py[co]
%{py_sitedir}/%{pname}/Geometry/*.py[co]
%{py_sitedir}/%{pname}/IO/*.py[co]
%{py_sitedir}/%{pname}/MPI/*.py[co]
%{py_sitedir}/%{pname}/Physics/*.py[co]
%{py_sitedir}/%{pname}/Statistics/*.py[co]
%{py_sitedir}/%{pname}/Threading/*.py[co]
%{py_sitedir}/%{pname}/TkWidgets/*.py[co]
%{py_sitedir}/%{pname}/Visualization/*.py[co]
%dir %{py_sitedir}/%{pname}/linux2
%attr(755,root,root) %{py_sitedir}/%{pname}/linux2/Scientific_netcdf.so
%{py_sitedir}/%{pname}/*.py[co]
%{py_incdir}/%{pname}
