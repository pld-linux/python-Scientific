%include	/usr/lib/rpm/macros.python

%define 	pname	Scientific
%define		mname	%{pname}Python

Summary:	Various Python modules for scientific computing
Summary(pl):	Ró¿ne modu³y Pythona dla obliczeñ naukowych
Name:		python-%{pname}
Version:	2.2
Release:	1
Group:		Libraries/Python
License:	LGPL
Source0:	http://starship.python.net/crew/hinsen/%{mname}-%{version}.tar.gz
Url:		http://starship.python.net/crew/hinsen/scientific.html
BuildRequires:	netcdf-devel
BuildRequires:	python-numpy
BuildRequires:	tkinter
Requires:	python-numpy
Requires:	tkinter
%requires_eq	python
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
python setup.py install \
	--root=$RPM_BUILD_ROOT

%{py_ocomp} $RPM_BUILD_ROOT%{py_sitedir}
%{py_comp} $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf README README.MPI

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Doc/HTML Doc/PDF
%dir %{py_sitedir}/%{pname}
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
