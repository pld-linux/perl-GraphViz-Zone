#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
%define		pnam	Zone
Summary:	GraphViz::Zone Perl module - interface to graphing hosts in BIND zone files
Summary(pl):	Modu� Perla GraphViz::Zone - interfejs do obrazowania host�w z plik�w stref BIND-a
Name:		perl-GraphViz-Zone
Version:	0.01
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GraphViz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GraphViz::Zone module - interface to graphing hosts in BIND zone
files.

%description -l pl
Modu� GraphViz::Zone - interfejs do obrazowania host�w z plik�w stref
BIND-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/GraphViz/Zone.pm
%{_mandir}/man3/*