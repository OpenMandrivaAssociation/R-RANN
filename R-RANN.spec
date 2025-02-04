%global packname  RANN
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.3.0
Release:          2
Summary:          Fast Nearest Neighbour Search
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/RANN_2.3.0.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
Finds the k nearest neighbours for every point in a given dataset in O(N
log N) time using Arya and Mount's ANN library (v1.1.1).  Two functions
allow searches for nearest neighbours within a point set or between two
separate point sets. There is support for approximate as well as exact
searches, fixed radius searches and bd as well as kd trees. This version
updates ANN 1.1.3 and fixes package compilation on Windows.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/COPYRIGHT
