#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
%define		pnam	Zone
Summary:	GraphViz::Zone Perl module - interface to graphing hosts in BIND zone files
Summary(pl):	Modu³ Perla GraphViz::Zone - interfejs do obrazowania hostów z plików stref BIND-a
Name:		perl-GraphViz-Zone
Version:	0.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	727c036d878aa6224ee825d7a77ee39b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GraphViz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GraphViz::Zone module - interface to graphing hosts in BIND zone
files.

%description -l pl
Modu³ GraphViz::Zone - interfejs do obrazowania hostów z plików stref
BIND-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
