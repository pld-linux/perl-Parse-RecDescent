#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	RecDescent
Summary:	Perl Parse::RecDescent module
Summary(pl):	Modu³ Perla Parse::RecDescent
Name:		perl-Parse-RecDescent
Version:	1.80
Release:	7
License:	Perl Artistic License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl-devel >= 5.6.1
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Text-Balanced

%define		_noautoreq	"perl(Calc)"

%description
Perl Parse::RecDescent module.

%description -l pl
Modu³ Perla Parse::RecDescent.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/Parse/*.pm
%{perl_sitelib}/Text/*.pm
%{_mandir}/man3/*
