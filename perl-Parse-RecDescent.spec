%include	/usr/lib/rpm/macros.perl
Summary:	Perl Parse::RecDescent module
Summary(pl):	Modu³ Perla Parse::RecDescent
Name:		perl-Parse-RecDescent
Version:	1.80
Release:	3
License:	Perl Artistic License
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Parse/Parse-RecDescent-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl-devel >= 5.6.1
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Text-Balanced

%define		_noautoreq	"perl(Calc)"

%description
Perl Parse::RecDescent module.

%description -l pl
Modu³ Perla Parse::RecDescent.

%prep
%setup -q -n Parse-RecDescent-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Parse/*
%{perl_sitelib}/Text/*
%{_mandir}/man3/*
